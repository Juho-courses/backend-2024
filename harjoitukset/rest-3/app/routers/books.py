from fastapi import APIRouter, status
from ..database.book_crud import BookBase, BookDb
from ..database import book_crud

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/", response_model=list[BookDb])
def get_books(author: str = ""):
    return book_crud.get_books(author)


@router.get("/{id}", response_model=BookDb)
def get_book(id: int):
    return book_crud.get_book(id)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_book(book_in: BookBase):
    return book_crud.save_book(book_in)


@router.delete("/{id}")
def delete_book(id: int):
    return book_crud.delete_book(id)
