from pydantic import BaseModel


class CreateSensor(BaseModel):
    name: str
    model: str
    data: str