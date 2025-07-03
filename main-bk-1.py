from typing import Any
from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference
from app.db import shipments
from app.schema import Shipment

app = FastAPI()

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
def get_shipments() -> dict[int, Any]:
    return shipments

@app.get("/shipments/{id}")
def get_shipments(id: int) -> Shipment:

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

