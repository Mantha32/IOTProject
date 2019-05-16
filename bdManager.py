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

     # Fetch five messages
    def get_messages(self):
        return self.session.query(Message).limit(5)

    # Fetch message between two datetimes
    def get_messages_between(self, start_date, end_date):
        return  self.session.query(Message).filter(Message.release_date >= start_date).filter(Message.release_date <= end_date)





