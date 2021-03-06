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
import datetime


class DbManager(object):
    def __init__(self):
        self.session = Session()
        self.devices = {}

    def generate_data_base(self):
        # Delete database file if it exists currently
        if os.path.exists("ttn.db"):
            os.remove("ttn.db")

        Base.metadata.create_all(engine)

     # Fetch five messages
    def get_messages(self):
        return self.session.query(Message).order_by(Message.id.desc()).limit(5)

    # Fetch message between two datetimes
    def get_messages_between(self, start_date, end_date):
        return self.session.query(Message).filter(Message.release_date >= start_date).filter(Message.release_date <= end_date)

    #  message from date_str to now
    def get_messages_from(self, date_str):
        return self.get_messages_between(date_str, datetime.datetime.now())

    # message for one specifique day
