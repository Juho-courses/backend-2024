from fastapi import APIRouter, status
from ..database.models import ManuBase, ManuDB
from ..database import manus_crud

router = APIRouter(prefix='/manufacturers')

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_manu(manu_in: ManuBase):
    return manus_crud.create_manu(manu_in)


@router.get("/", response_model=list[ManuDB])
def get_manus():
    return manus_crud.get_manus()


@router.get("/{id}", response_model=ManuDB)
def get_manu(id: int):
    return manus_crud.get_manu(id)


@router.delete("/{id}")
def delete_manu(id: int):
    return manus_crud.delete_manu(id)