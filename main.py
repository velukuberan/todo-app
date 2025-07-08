from typing import Any
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from scalar_fastapi import get_scalar_api_reference
from app.user.route import router as user_router 
from app.book.route import router as book_router
from app.shipment.route import router as shipping_router
import os

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:3000",
    "http://frontend:3000",
    "http://127.0.0.1:3000",
]

# Allow CORS_ORIGINS environment variable to override
cors_origins = os.getenv("CORS_ORIGINS")
if cors_origins:
    origins.extend(cors_origins.split(","))

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "message": "Todo App Backend (Python 3.7) is running!"
    }

@app.get("/documentations", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API"
    )

app.include_router(user_router, prefix="/api/v1")
app.include_router(book_router, prefix="/api/v1")
app.include_router(shipping_router, prefix="/api/v1")
