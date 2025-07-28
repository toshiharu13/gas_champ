from pydantic import BaseModel


class CreateSensor(BaseModel):
    name: str = None
    model: str = None
    data: str = None

class CreateDevice(BaseModel):
    name: str
    model: str
    place: str