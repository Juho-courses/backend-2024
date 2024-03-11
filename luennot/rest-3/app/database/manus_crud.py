from fastapi import HTTPException
from .models import ManuBase, ManuDB

manus = {
    0: {"id": 0, "name": "Nike"},
    1: {"id": 1, "name": "Hoka"},
}

def create_manu(manu_in: ManuBase):
    new_id = max(manus.keys()) + 1
    manu = ManuDB(**manu_in.model_dump(), id=new_id)
    manus[new_id] = manu.model_dump()
    return manu

def get_manus():
    return [manus[s] for s in manus]

def get_manu(id: int):
    if id not in manus:
        raise HTTPException(status_code=404, detail=f"{id} not found")
    return manus[id]

def delete_manu(id: int):
    if id not in manus:
        raise HTTPException(status_code=404, detail='ID not found')
    del manus[id]
    return {'message': f'manufacturer with id {id} deleted'}