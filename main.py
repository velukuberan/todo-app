from typing import Any
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from scalar_fastapi import get_scalar_api_reference
from app.db import shipments
from app.schema import Shipment
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

@app.get("/shipments")
def get_all_shipments() -> "dict[int, Any]":
    return shipments

@app.get("/shipments/{id}")
def get_shipment_by_id(id: int) -> Shipment:

    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Shipment #id:{id} doesn't exists"
        )

    return Shipment(
        **shipments[id]
    )

@app.post("/shipments")
def create_shipments(shipment: Shipment) -> Shipment:
    new_id = max(shipments.keys()) + 1

    shipments[new_id] = {
        "content": shipment.content,
        "weight": shipment.weight,
        "destination": shipment.destination,
        "status": shipment.status
    }

    return Shipment(
        **shipments[new_id]
    )

