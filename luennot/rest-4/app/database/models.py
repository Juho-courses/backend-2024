from pydantic import BaseModel
from sqlmodel import SQLModel, Field


class ShoeBase(SQLModel):
    model: str
    manufacturer: str


class ShoeDB(ShoeBase, table=True):
    id: int = Field(default=None, primary_key=True)


class ShoeCreate(ShoeBase):
    pass


class ManuBase(SQLModel):
    name: str


class ManuDB(ManuBase, table=True):
    id: int = Field(default=None, primary_key=True)
