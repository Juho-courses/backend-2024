from fastapi import HTTPException
from .models import ShoeDB, ShoeBase, ShoeCreate
from sqlmodel import Session, select


def create_shoe(session: Session, shoe_in: ShoeCreate):
    shoe_db = ShoeDB.model_validate(shoe_in)
    session.add(shoe_db)
    session.commit()
    session.refresh(shoe_db)
    return shoe_db


def get_shoes(session: Session, manufacturer: str = ""):
    if manufacturer != "":
        return session.exec(select(ShoeDB).where(ShoeDB.manufacturer == manufacturer)).all()
    return session.exec(select(ShoeDB)).all()


def get_shoe(session: Session, id: int):
    shoe = session.get(ShoeDB, id)
    if not shoe:
        raise HTTPException(status_code=404, detail=f"{id} not found")
    return shoe


def delete_shoe(session: Session, id: int):
    shoe = session.get(ShoeDB, id)
    if not shoe:
        raise HTTPException(status_code=404, detail='ID not found')
    session.delete(shoe)
    session.commit()
    return {'message': f'Shoe with id {id} deleted'}
