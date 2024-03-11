from fastapi import HTTPException
from .models import ShoeDB, ShoeBase

shoes = {
    0: {"id": 0, "model": "Speedgoat 5", "manufacturer": "Hoka"},
    1: {"id": 1, "model": "Air Zoom", "manufacturer": "Nike"},
    2: {"id": 2, "model": "Speedgoat 4", "manufacturer": "Hoka"},
}

def create_shoe(shoe_in: ShoeBase):
    new_id = max(shoes.keys()) + 1
    shoe = ShoeDB(**shoe_in.model_dump(), id=new_id)
    shoes[new_id] = shoe.model_dump()
    return shoe

def get_shoes(manufacturer: str = ""):
    if manufacturer != "":
        return [shoes[s] for s in shoes if shoes[s]['manufacturer'] == manufacturer]
    return [shoes[s] for s in shoes]

def get_shoe(id: int):
    if id not in shoes:
        raise HTTPException(status_code=404, detail=f"{id} not found")
    return shoes[id]

def delete_shoe(id: int):
    if id not in shoes:
        raise HTTPException(status_code=404, detail='ID not found')
    del shoes[id]
    return {'message': f'Shoe with id {id} deleted'}