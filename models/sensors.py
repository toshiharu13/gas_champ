from backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from sqlalchemy.schema import CreateTable
from models.devices import Device



class FirstSensor(Base):
    __tablename__ = 'sensor'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    model = Column(String)
    data = Column(String)
    active = Column(Boolean, default=True)
    device_id = Column(Integer, ForeignKey('device.id'))

    devices = relationship('Device', back_populates='sensors')

print(CreateTable(FirstSensor.__table__))