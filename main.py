from typing import Any
from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference
from app.db import shipments

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Todo App Backend (Python 3.7) is running!"
    }

@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API"
    )

@app.get("/shipments")
def get_shipment(id: int | None = None):
    if not id:
        id = max(shipments.keys())

    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shipment id doesn't exists."
        )

    return shipments[id]

@app.post("/shipments")
def new_shipment(data: dict[str, Any]) -> dict[str, int]:

    content = data['content']
    weight = data['weight']

    if weight > 25:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Maximum weight limit is 25 kgs"
        )

    new_id = max(shipments.keys()) + 1

    shipments[new_id] = {
        "content": content,
        "weight": weight,
        "status": "placed"
    }
    
    return {"id": new_id}

@app.put("/shipments/{id}")
def update_shipment(id: int, data: dict[str, Any]) -> dict[str, Any]:  # Fixed return type
    
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shipment id doesn't exist."
        )
     
    if 'weight' in data and data['weight'] > 25:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Maximum weight limit is 25 kgs"
        )
    
    # Update existing shipment instead of replacing
    shipment = shipments[id]
    shipment.update(data)
    shipments[id] = shipment

    return shipments[id]

@app.delete("/shipments/{id}")
def delete_shipments(id: int) -> dict[str, str]:
    
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shipment id doesn't exist."
        )
     
    shipments.pop(id)
    return {
        "details": f"Shipment with id #{id} is deleted!"
    }
