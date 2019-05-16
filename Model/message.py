"""
Class Message

relation many to one with back populate the device
mayn message to one device
Param:
    app_id : the application name from TTN
    app_eui:
"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from Model.base import Base
from sqlalchemy.orm import relationship



class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    app_id = Column('app_id', String)
    dev_id = Column('dev_id', String)
    dev_eui = Column('dev_eui', String)
    port = Column('port', Integer)
    payload = Column('payload', String)
    release_date = Column('release_date', DateTime)
    #dev_bd_id = Column(Integer, ForeignKey('device.id'))
    #device = relationship("Device", backref="Message") # many messages to one device

    def __init__(self,app_id, dev_id, dev_eui, port,payload, release_date):
        self.app_id = app_id
        self.dev_id = dev_id
        self.dev_eui = dev_eui
        self.port = port
        self.payload = payload
        self.release_date = release_date


    def get_name(self):
        return self.dev_id;

    def get_eui(self):
        return self.dev_eui