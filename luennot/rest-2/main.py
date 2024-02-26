from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

shoes = {
    0: {"id": 0, "model": "Speedgoat 5", "manufacturer": "Hoka"},
    1: {"id": 1, "model": "Air Zoom", "manufacturer": "Nike"},
    2: {"id": 2, "model": "Speedgoat 4", "manufacturer": "Hoka"},
}


class ShoeBase(BaseModel):
    model: str
    manufacturer: str


class ShoeDB(ShoeBase):
    id: int


@app.post("/shoes", status_code=status.HTTP_201_CREATED)
def create_shoe(shoe_in: ShoeBase):
    new_id = max(shoes.keys()) + 1
    shoe = ShoeDB(**shoe_in.model_dump(), id=new_id)
    shoes[new_id] = shoe.model_dump()
    return shoe


# /shoes?manufacturer=Hoka
@app.get("/shoes", response_model=list[ShoeDB])
def get_shoes(manufacturer: str = ""):
    if manufacturer != "":
        return [shoes[s] for s in shoes if shoes[s]['manufacturer'] == manufacturer]
    return [shoes[s] for s in shoes]


@app.get("/shoes/{id}", response_model=ShoeDB)
def get_shoe(id: int):
    return shoes[id]


@app.delete("/shoes/{id}")
def delete_shoe(id: int):
    if id not in shoes:
        raise HTTPException(status_code=404, detail='ID not found')
    del shoes[id]
    return {'message': f'Shoe with id {id} deleted'}
