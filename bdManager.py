"""
Class DbManager
this API expose the CRUD that we need
manipulate app, device and message object

Param:
    app_id : the application name from TTN
    app_eui:
"""

import os
from Model.base import Session, Base, engine
from Model.message import Message
from Model.device import Device
from Model.application import Application


class DbManager(object):
    def __init__(self):
        self.session = Session
        self.devices = {}


    def generate_data_base(self):
        # Delete database file if it exists currently
        if os.path.exists("ttn.db"):
            os.remove("ttn.db")

        Base.metadata.create_all(engine)

    def add_application(self, application):
        session_local = self.session()
        session_local.add(application)
        session_local.commit()
        session_local.close()


    def get_devices(self):
        session_local = self.session()
        result = self.session.query(Device).join(Application).all()
        session_local.commit()
        session_local.close()
        return result

    def get_device_by_dev_id(self, dev_id):
        session_local = self.session()
        result = self.session.query(Device).join(Application).filter(Device.dev_id == dev_id)
        session_local.commit()
        session_local.close()
        return result

    def update_description_device(self, device, description):
        session_local = self.session()
        session_local.query(Device).join(Application).filter(Device.dev_id == device.dev_id).update({Device.description: description}, synchronize_session = False )
        session_local.commit()
        session_local.close()

    def add_message(self, message):


     # Fetch five messages
    def get_messages(self):
        return self.session.query(Message).join(Device).join(Application).limit(5)

    # Fetch message between two datetimes
    def get_messages_between(self, start_date, end_date):
        return  self.session.query(Message).join(Device).join(Application).filter(Message.release_date >= start_date).filter(Message.release_date <= end_date)





