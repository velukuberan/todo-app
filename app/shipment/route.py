from typing import Any, List
from fastapi import APIRouter, HTTPException, status
from app.db import shipments
from .schema import Shipment, ShipmentPatch

router = APIRouter(prefix="/shipments", tags=["shipments"])

@router.get("/", response_model=List[Shipment])
def get_all_shipments(): 
    return [Shipment(**data) for data in shipments.values()] 

@router.get("/{id}", response_model=Shipment)
def get_shipment_by_id(id: int):

    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Shipment #id:{id} doesn't exists"
        )

    return Shipment(
        **shipments[id]
    )

@router.post("/", response_model=Shipment)
def create_shipments(shipment: Shipment):
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

@router.put("/{id}", response_model=Shipment)
def shipment_update(id: int, body: Shipment):
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Shipment #id:{id} doesn't exists"
        )
    
    shipments[id].update(body)

    return Shipment(
        **shipments[id]
    )

@router.patch("/{id}", response_model=Shipment)
def shipment_patch(id: int, body: ShipmentPatch):
    shipment = shipments[id]
    shipment.update(body)
    return shipment


@router.delete("/{id}")
def shipment_delete(id: int):
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Shipment #id:{id} doesn't exists"
        )
    
    shipments.pop(id)

    return {"detail": f"Shipment with id {id} is deleted"}
