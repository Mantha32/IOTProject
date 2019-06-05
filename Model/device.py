"""
Class Device derived from application

Param:
    app_id : the application name from TTN
    app_eui:
"""

from sqlalchemy import Column, Integer, String, ForeignKey

from Model.base import Base
from sqlalchemy.orm import relationship


class Device(Base):
    __tablename__ = 'device'
    id = Column(Integer, primary_key=True)
    dev_id = Column('dev_id', String(64))   # the device name
    dev_eui = Column('dev_eui', String(64))  # hardware_serial for the device
    description = Column('description', String)

    # ref to app id , relationship in db table
    app_id = Column(Integer, ForeignKey('application.id'))
    # relationship many devices to one application
    application = relationship("Application", backref="device")

    def __init__(self, dev_id, dev_eui, description, my_app):
        self.dev_id = dev_id
        self.dev_eui = dev_eui
        self.description = description
        self.application = my_app

    def get_name(self):
        return self.dev_id

    def get_eui(self):
        return self.dev_eui

    def get_description(self):
        return self.description
