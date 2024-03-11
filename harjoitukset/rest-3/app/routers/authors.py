from fastapi import APIRouter, status
from ..database.author_crud import (
    fetch_author,
    fetch_authors,
    save_author,
    delete_author,
)
from ..database.models import AuthorDb, AuthorBase


router = APIRouter(prefix="/authors")


@router.get("/", response_model=list[AuthorDb])
def get_authors():
    return fetch_authors()


@router.get("/{id}", response_model=AuthorDb)
def get_author(id: int):
    return fetch_author(id)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_author(author_in: AuthorBase):
    return save_author(author_in)


@router.delete("/")
def remove_author(id: int):
    return delete_author(id)
