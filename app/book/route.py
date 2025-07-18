from typing import List
from fastapi import APIRouter, HTTPException, status
from .schema import Book 
from .db import books

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/", response_model=List[Book])
def get_all_books():
    return [
        Book(id=book_id, **data) for book_id, data in books.items()
    ]

@router.get("/{id}", response_model=Book)
def get_book_by_id(id: int):

    if id not in books:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book #id:{id} doesn't exists"
        )

    book = Book(
        id=id,
        **books[id]
    )
    
    book.add_genre('Thriller')

    return book
