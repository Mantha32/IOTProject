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
    payload = Column('payload', String)
    release_date = Column('release_date', DateTime)
    dev_bd_id = Column(Integer, ForeignKey('device.id'))
    device = relationship("Device", backref="Message") # many messages to one device

    def __init__(self,payload, release_date,device):
        self.payload = payload
        self.release_date = release_date
        self.device = device

    def get_name(self):
        return self.dev_id;

    def get_eui(self):
        return self.dev_eui