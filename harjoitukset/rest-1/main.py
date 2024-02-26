from fastapi import FastAPI

app = FastAPI()

books = {
    1: {"id": 1, "name": "Book1", "author": "Author1"},
    2: {"id": 2, "name": "Book2", "author": "Author2"},
    3: {"id": 3, "name": "Book3", "author": "Author2"},
}


@app.get("/books")
def get_books(author: str = ""):
    if author != "":
        return [books[b] for b in books if books[b]["author"] == author]
    return books


@app.get("/books/{id}")
def get_book(id: int):
    return books[id]
