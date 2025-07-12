from backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean

from sqlalchemy.schema import CreateTable



class FirstModel(Base):
    __tablename__ = 'ml_monitor'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    model = Column(String)

print(CreateTable(FirstModel.__table__))