from fastapi import APIRouter

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/")
def get_books():
    return {
        "message": "Books endpoint"
    }
