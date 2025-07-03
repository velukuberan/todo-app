from fastapi import APIRouter

router = APIRouter(prefix="/shippings", tags=["shippings"])

@router.get("/")
def get_shippings():
    return {
        "message": "Shippings endpoint"
    }
