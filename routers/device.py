from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from sqlalchemy import insert, select, update, Update, delete

from backend.db_depends import get_db
from models import Device
from sсhemas import CreateDevice

#from sсhemas import CreateDevice

router = APIRouter(prefix='/device', tags=['Devices'])

@router.get('/all_devices')
async def get_all_devices(db: Annotated[Session, Depends(get_db)]):
    query = select(Device).where(Device.active == True)
    devices = db.scalars(query).all()
    return devices

@router.post('create', status_code=status.HTTP_201_CREATED)
async def create_device(db: Annotated[Session, Depends(get_db)], create_device: CreateDevice):
    db.execute(insert(Device).values(
        name=create_device.name,
        model=create_device.model,
        place=create_device.place))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }

@router.get('/detail/{divice_id}')
async def device_detail(db: Annotated[Session, Depends(get_db)], divice_id: int):
    query = select(Device).where(Device.id == divice_id)
    current_device = db.scalar(query)
    current_device = {
        "model": current_device.model,
        "id": current_device.id,
        "name": current_device.name,
        "place": current_device.place,
        "active": current_device.active,
        "sensors": current_device.sensors
    }
    return current_device

@router.delete('/delete/{divice_id}')
async def delete_device(db: Annotated[Session, Depends(get_db)], divice_id: int):
    query = delete(Device).where(Device.id == divice_id)
    db.execute(query)
    db.commit()
    return {
        'status_code': status.HTTP_204_NO_CONTENT,
        'transaction': 'Successful'
    }

@router.put('/update/{divice_id}')
async def update_device(db: Annotated[Session, Depends(get_db)], divice_id: int, update_device: CreateDevice):
    query = Update(Device).where(Device.id == divice_id).values(
        name=update_device.name,
        model=update_device.model,
        place=update_device.place,
    )
    db.execute(query)
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Successful'
    }

@router.patch('/update_sensors/{divice_id}')
async def update_device_sensors(db: Annotated[Session, Depends(get_db)], divice_id: int, update_device_sensors: list):
    query = Update(Device).where(Device.id == divice_id).values(
        sensors=update_device_sensors
    )
    db.execute(query)
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Successful'
    }