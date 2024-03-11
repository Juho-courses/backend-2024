from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()


books = {
    1: {"id": 1, "name": "Book1", "author": "Author1"},
    2: {"id": 2, "name": "Book2", "author": "Author2"},
    3: {"id": 3, "name": "Book3", "author": "Author2"},
}


class BookBase(BaseModel):
    name: str
    author: str


class BookDb(BookBase):
    id: int


@app.get("/books", response_model=list[BookDb])
def get_books(author: str = ""):
    if author != "":
        return [books[b] for b in books if books[b]["author"] == author]
    return [books[b] for b in books]


@app.get("/books/{id}", response_model=BookDb)
def get_book(id: int):
    if id not in books:
        raise HTTPException(status_code=404, detail=f"Book with id {id} not found")
    return books[id]


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book_in: BookBase):
    new_id = max(books.keys()) + 1
    book = BookDb(**book_in.model_dump(), id=new_id)
    books[new_id] = book.model_dump()
    return book


@app.delete("/books/{id}")
def delete_book(id: int):
    if id not in books:
        raise HTTPException(status_code=404, detail=f"Book with id {id} not found")
    del books[id]
    return {"message": f"Book {id} deleted."}
