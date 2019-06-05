"""
Class Application
Relationship one to many
on application may have any devices

Param:
    app_id : the application name from TTN
    app_eui:
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Model.base import Base


class Application(Base):
    __tablename__ = 'application'

    id = Column(Integer, primary_key=True)
    app_id = Column('app_id', String(64))
    app_eui = Column('app_eui', String(64))

    def __init__(self, app_id, app_eui):
        self.app_id = app_id
        self.app_eui = app_eui

    def get_eui(self):
        return self.app_eui

    def get_name(self):
        return self.app_id
