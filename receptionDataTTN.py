import time
import ttn
import os
import datetime
from datetime import date
from Model.application import Application
from Model.device import Device
from Model.message import Message
from Configuration.configueApp import app_id, access_key
from utility import decoder,hex_to_string, iso_to_datetime, remove_payload_header
from Model.base import Session, Base, engine
from dbManager import DbManager


# Dictionary of register device
device_dico = {}


handler = ttn.HandlerClient(app_id, access_key)


# using application manager client
# Create my_app
# Creates an ApplicationClient object
app_client = handler.application()
my_app_name = app_client.get()
my_devices = app_client.devices()

my_app_eui = hex_to_string(my_devices[0].lorawan_device.app_eui)

# Create object app for record databse purpose
my_app = Application(app_client.app_id, str(my_app_eui))


# create a new session
session = Session()

# Add my application
session.add(my_app)

my_devices = app_client.devices()

# Add all devices  in database
for device in my_devices:
    # Create device
    dev_eui = hex_to_string(device.lorawan_device.dev_eui)

    # add device to my_application
    my_device = Device(device.dev_id, dev_eui, device.description, my_app)
    device_dico[device.dev_id] = my_device
    # Persist data in database
    session.add(my_device)

message_fixture = Message("ttn 2019", "device sample", "serial number", 1, remove_payload_header("ENV#","ENV#hello world"), datetime.datetime.now())
session.add(message_fixture)


# commit and close session
session.commit()
session.close()


# using mqtt client: handler.data return Mqtt_client() which wraps paho.mqtt.client
# reconnect: boolean whether to automatically reconnect to the MQTT server on unexpected disconnect
# (useful if you'd like to keep the connection alive for several hours)
mqtt_client = handler.data(reconnect=True)

# handle the uplink message, record in database
def uplink_callback(msg, client):
    print(msg)
    payload = decoder(msg.payload_raw)
    print("payload value: ", payload)
    print("time value: ",msg.metadata.time)
    start_payload = "Starting payload..."
    payload_header = "ENV#"
    print("timestamp: ", iso_to_datetime(msg.metadata.time))
    if(start_payload not in payload):
        if(payload_header in payload):
            payload = remove_payload_header(payload_header, payload)

        message = Message(msg.app_id, msg.dev_id, msg.hardware_serial, msg.port, payload, iso_to_datetime(msg.metadata.time))
        session_tmp = Session()
        session_tmp.add(message)
        session_tmp.commit()
        session_tmp.close()

# Record the message from each running device
mqtt_client.set_uplink_callback(uplink_callback)


mqtt_client.start()

mqtt_client.connect()

# Manage the loop connexion to the broker
# MQTT client is based on paho.mqtt.client: We add loop_forever method in ttn lib (ttnmqtt.py) which wraps paho.mqtt.client.loop_forever()
#mqtt_client.loop_forever()

database_manager = DbManager()

print("get 5 last messages: ")
result = database_manager.get_messages()
for row in result:
    print("id: ",row.id ,"name device:", row.dev_id, "payload" , row.payload , "timestamp: " , row.release_date)

print("get messages for today: ")
result = database_manager.get_messages(date.today())
for row in result:
    print(row)

print("get messages between two day: ")
result = database_manager.get_messages("2019-05-23 17:30:21", datetime.datetime.now())
for row in result:
    print(row)


