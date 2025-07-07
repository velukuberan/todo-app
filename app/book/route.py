from typing import List
from fastapi import APIRouter
from .schema import BaseBook
from .db import books

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/", response_model=List[BaseBook])
def get_books():
    return [
        BaseBook(**data) for data in books.values()
    ]

@router.get("/{id}", response_model=BaseBook)
def get_books(id: int):

    if id not in books:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book #id:{id} doesn't exists"
        )

    return BaseBook(
        **books[id]
    )

