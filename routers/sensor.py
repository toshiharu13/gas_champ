from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from sqlalchemy import insert, select, update

from models import FirstSensor
from backend.db_depends import get_db
from models import FirstSensor
from sсhemas import CreateSensor

router = APIRouter(prefix='/sensor', tags=['monotoring'])


@router.get('/all_sensors')
async def default_request(db: Annotated[Session, Depends(get_db)]):
    query = select(FirstSensor).where(FirstSensor.active == True)
    sensors = db.scalars(query).all()
    return sensors

@router.post('create', status_code=status.HTTP_201_CREATED)
async def create_category(db: Annotated[Session, Depends(get_db)], create_sensor: CreateSensor):
    db.execute(insert(FirstSensor).values(
        name=create_sensor.name,
        model=create_sensor.model,
        data=create_sensor.data))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }