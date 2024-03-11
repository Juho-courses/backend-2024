from pydantic import BaseModel

class ManuBase(BaseModel):
    name: str

class ManuDB(ManuBase):
    id: int

class ShoeBase(BaseModel):
    model: str
    manufacturer: str


class ShoeDB(ShoeBase):
    id: int
