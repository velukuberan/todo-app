from typing import Any
from fastapi import APIRouter
from app.db import shipments
from .schema import Shipment

router = APIRouter(prefix="/shipments", tags=["shipments"])

@router.get("/")
def get_shipments() -> dict[int, Any]:
    return shipments

@router.get("/{id}")
def get_shipments(id: int) -> Shipment:

    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Shipment #id:{id} doesn't exists"
        )

    return Shipment(
        **shipments[id]
    )

@router.post("/")
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

