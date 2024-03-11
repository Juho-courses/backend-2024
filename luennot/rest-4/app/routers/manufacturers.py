from fastapi import APIRouter, status, Depends
from ..database.models import ManuBase, ManuDB
from ..database import manus_crud
from ..database.database import get_session
from sqlmodel import Session

router = APIRouter(prefix='/manufacturers')


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_manu(*, session: Session = Depends(get_session), manu_in: ManuBase):
    return manus_crud.create_manu(session, manu_in)


@router.get("/", response_model=list[ManuDB])
def get_manus(session: Session = Depends(get_session)):
    return manus_crud.get_manus(session)


@router.get("/{id}", response_model=ManuDB)
def get_manu(id: int):
    return manus_crud.get_manu(id)


@router.delete("/{id}")
def delete_manu(id: int):
    return manus_crud.delete_manu(id)
