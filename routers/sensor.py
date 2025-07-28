from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from sqlalchemy import insert, select, update, Update, delete

from backend.db_depends import get_db
from models import FirstSensor
from sсhemas import CreateSensor

router = APIRouter(prefix='/sensor', tags=['Sensors'])


@router.get('/all_sensors')
async def get_all_sensors(db: Annotated[Session, Depends(get_db)]):
    query = select(FirstSensor).where(FirstSensor.active == True)
    sensors = db.scalars(query).all()
    return sensors

@router.post('create', status_code=status.HTTP_201_CREATED)
async def create_sensor(db: Annotated[Session, Depends(get_db)], create_sensor: CreateSensor):
    db.execute(insert(FirstSensor).values(
        name=create_sensor.name,
        model=create_sensor.model,
        data=create_sensor.data))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }

@router.get('/detail/{sensor_id}')
async def sensor_detail(db: Annotated[Session, Depends(get_db)], sensor_id: int):
    query = select(FirstSensor).where(FirstSensor.id == sensor_id )
    current_sensor = db.scalar(query)
    return current_sensor

@router.delete('/delete/{sensor_id}')
async def delete_sensor(db: Annotated[Session, Depends(get_db)], sensor_id: int):
    query = delete(FirstSensor).where(FirstSensor.id == sensor_id)
    db.execute(query)
    db.commit()
    return {
        'status_code': status.HTTP_204_NO_CONTENT,
        'transaction': 'Successful'
    }

@router.patch('/update/{sensor_id}')
async def update_sensor(db: Annotated[Session, Depends(get_db)], sensor_id: int, update_sensor: CreateSensor):
    update_data = update_sensor.dict(exclude_unset=True)
    query = select(FirstSensor).where(FirstSensor.id == sensor_id)
    current_sensor = db.scalar(query)

    for key, value in update_data.items():
        setattr(current_sensor, key, value)
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Successful'
    }


@router.get('/turn_on/{sensor_id}')
async def turn_on_sensor(db: Annotated[Session, Depends(get_db)],sensor_id: int):
    query = Update(FirstSensor).where(FirstSensor.id == sensor_id).values(
        active=True
    )
    db.execute(query)
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Successful'
    }

@router.get('/turn_off/{sensor_id}')
async def turn_on_sensor(db: Annotated[Session, Depends(get_db)],sensor_id: int):
    query = Update(FirstSensor).where(FirstSensor.id == sensor_id).values(
        active=False
    )
    db.execute(query)
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Successful'
    }