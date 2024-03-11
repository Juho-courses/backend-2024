from fastapi import APIRouter, status, Depends
from sqlmodel import Session
from ..database.models import ShoeBase, ShoeDB, ShoeCreate
from ..database import shoes_crud
from ..database.database import get_session

router = APIRouter(prefix='/shoes')


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_shoe(*, session: Session = Depends(get_session), shoe_in: ShoeCreate):
    shoe = shoes_crud.create_shoe(session, shoe_in)
    return shoe


# /shoes?manufacturer=Hoka
@router.get("/", response_model=list[ShoeDB])
def get_shoes(*, session: Session = Depends(get_session), manufacturer: str = ""):
    shoes = shoes_crud.get_shoes(session, manufacturer)
    return shoes


@router.get("/{id}", response_model=ShoeDB)
def get_shoe(*, session: Session = Depends(get_session), id: int):
    return shoes_crud.get_shoe(session, id)


@router.delete("/{id}")
def delete_shoe(*, session: Session = Depends(get_session), id: int):
    return shoes_crud.delete_shoe(session, id)
