from fastapi import HTTPException
from .models import BookBase, BookDb


books = {
    1: {"id": 1, "name": "Book1", "author": "Author1"},
    2: {"id": 2, "name": "Book2", "author": "Author2"},
    3: {"id": 3, "name": "Book3", "author": "Author2"},
}


def get_books(author: str = ""):
    if author != "":
        return [books[b] for b in books if books[b]["author"] == author]
    return [books[b] for b in books]


def get_book(id: int):
    if id not in books:
        raise HTTPException(status_code=404, detail=f"Book with id {id} not found")
    return books[id]


def save_book(book_in: BookBase):
    new_id = max(books.keys()) + 1
    book = BookDb(**book_in.model_dump(), id=new_id)
    books[new_id] = book.model_dump()
    return book


def delete_book(id: int):
    if id not in books:
        raise HTTPException(status_code=404, detail=f"Book with id {id} not found")
    del books[id]
    return {"message": f"Book {id} deleted."}
