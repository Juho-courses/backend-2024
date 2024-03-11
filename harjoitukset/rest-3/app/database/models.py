from pydantic import BaseModel


class BookBase(BaseModel):
    name: str
    author: str


class BookDb(BookBase):
    id: int


class AuthorBase(BaseModel):
    name: str


class AuthorDb(AuthorBase):
    id: int
