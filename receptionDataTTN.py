import time
import ttn
import os

from Model.application import Application
from Model.device import Device
from Model.message import Message
from Configuration.configueApp import app_id, access_key
from utility import decoder,hex_to_string
from Model.base import Session, Base, engine


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

# Create object app
my_app = Application(app_client.app_id, str(my_app_eui))

# Delete database file if it exists currently
if os.path.exists("ttn.db"):
    os.remove("ttn.db")


# generate database schema
Base.metadata.create_all(engine)

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

print(device_dico.keys())
print(device_dico.values())

# commit and close session
session.commit()
session.close()


# using mqtt client
mqtt_client = handler.data()

# handle the uplink message, record in database
def uplink_callback(msg, client):
  print(msg)
  # create device
    tmp_device = Device(msg.)
  # add message to device
  message_device = Message(decoder(msg.payload_raw), msg.metadata.time, device)
  session.add(message_device)





# Record the message from each running device
mqtt_client.set_uplink_callback(uplink_callback)
mqtt_client.connect()
time.sleep(60)
mqtt_client.close()

