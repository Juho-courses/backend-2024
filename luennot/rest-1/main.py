from fastapi import FastAPI

app = FastAPI()

shoes = {
    0: {"id": 0, "model": "Speedgoat 5", "manufacturer": "Hoka"},
    1: {"id": 1, "model": "Air Zoom", "manufacturer": "Nike"},
    2: {"id": 2, "model": "Speedgoat 4", "manufacturer": "Hoka"},
}


# /shoes?manufacturer=Hoka
@app.get("/shoes")
def get_shoes(manufacturer: str = ""):
    if manufacturer != "":
        return [shoes[s] for s in shoes if shoes[s]['manufacturer'] == manufacturer]
    return [shoes[s] for s in shoes]


@app.get("/shoes/{id}")
def get_shoe(id: int):
    return shoes[id]
