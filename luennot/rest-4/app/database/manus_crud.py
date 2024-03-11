from fastapi import HTTPException
from .models import ManuBase, ManuDB
from sqlmodel import Session, select

manus = {
    0: {"id": 0, "name": "Nike"},
    1: {"id": 1, "name": "Hoka"},
}


def create_manu(session: Session, manu_in: ManuBase):
    manudb = ManuDB.model_validate(manu_in)
    session.add(manudb)
    session.commit()
    session.refresh(manudb)
    return manudb


def get_manus(session: Session):
    return session.exec(select(ManuDB)).all()


def get_manu(id: int):
    if id not in manus:
        raise HTTPException(status_code=404, detail=f"{id} not found")
    return manus[id]


def delete_manu(id: int):
    if id not in manus:
        raise HTTPException(status_code=404, detail='ID not found')
    del manus[id]
    return {'message': f'manufacturer with id {id} deleted'}
