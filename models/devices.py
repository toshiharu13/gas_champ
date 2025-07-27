from backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from sqlalchemy.schema import CreateTable


class Device(Base):
    __tablename__ = 'device'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    model = Column(String)
    place= Column(String)
    active = Column(Boolean, default=True)

    sensors = relationship('FirstSensor', back_populates='devices')