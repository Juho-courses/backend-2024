from fastapi import APIRouter, status, HTTPException
from ..database.models import ShoeBase, ShoeDB
from ..database import shoes_crud

router = APIRouter(prefix='/shoes')

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_shoe(shoe_in: ShoeBase):
    shoe =shoes_crud.create_shoe(shoe_in)
    return shoe


# /shoes?manufacturer=Hoka
@router.get("/", response_model=list[ShoeDB])
def get_shoes(manufacturer: str = ""):
    shoes = shoes_crud.get_shoes(manufacturer)
    return shoes


@router.get("/{id}", response_model=ShoeDB)
def get_shoe(id: int):
    return shoes_crud.get_shoe(id)


@router.delete("/{id}")
def delete_shoe(id: int):
    return shoes_crud.delete_shoe(id)