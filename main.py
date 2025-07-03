from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from app.user.route import router as user_router 
from app.book.route import router as book_router
from app.shipping.route import router as shipping_router 

app = FastAPI()
app.include_router(user_router, prefix="/api/v1")
app.include_router(book_router, prefix="/api/v1")
app.include_router(shipping_router, prefix="/api/v1")

@app.get("/documentations", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API"
    )

