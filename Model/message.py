"""
Class Message

relation many to one with back populate the device
many message to one device
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
    msg_id = Column('msg_id', String)
    
    dev_id = Column(Integer, ForeignKey("device.id"))
    device = relationship("Device", backref="message")

    port = Column('port', Integer)
    payload = Column('payload', String)
    release_date = Column('release_date', DateTime)

    def __init__(self, device, port, payload, release_date):
        self.device = device
        self.port = port
        self.payload = payload
        self.release_date = release_date

    def get_name(self):
        return self.dev_id

    def get_eui(self):
        return self.dev_eui
