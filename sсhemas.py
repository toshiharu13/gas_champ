from pydantic import BaseModel


class CreateSensor(BaseModel):
    name: str = None
    model: str = None
    data: str = None

class CreateDevice(BaseModel):
    name: str = None
    model: str = None
    place: str = None

class AddSensorsForDevice(BaseModel):
    sensor_ids : list[int]