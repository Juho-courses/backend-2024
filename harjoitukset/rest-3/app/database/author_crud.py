from fastapi import HTTPException
from .models import AuthorBase, AuthorDb

authors = {
    0: {"id": 0, "name": "Author0"},
    1: {"id": 1, "name": "Author1"},
    2: {"id": 2, "name": "Author2"},
}


def fetch_authors():
    return [authors[a] for a in authors]


def fetch_author(id: int):
    if id not in authors:
        raise HTTPException(status_code=404, detail=f"Author {id} not found.")
    return authors[id]


def save_author(author_in: AuthorBase):
    new_id = max(authors.keys()) + 1
    author = AuthorDb(**author_in.model_dump(), id=new_id)
    authors[new_id] = author.model_dump()
    return author


def delete_author(id: int):
    if id not in authors:
        raise HTTPException(status_code=404, detail=f"Author {id} not found.")
    del authors[id]
    return {"message": f"Author {id} deleted."}
