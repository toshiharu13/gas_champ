from backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean

from sqlalchemy.schema import CreateTable



class FirstSensor(Base):
    __tablename__ = 'sensor'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    model = Column(String)
    data = Column(String)
    active = Column(Boolean, default=True)

print(CreateTable(FirstSensor.__table__))