from random import randint
from enum import Enum
from pydantic import BaseModel, Field

def random_destination():
    return randint(1, 1000000)

class ShipmentStatus(str, Enum):
    placed = "placed"
    transit = "transit"
    processing = "processing"
    out_of_delivery = "out of delivery"
    completed = "completed"

class Shipment(BaseModel):
    content: str = Field(max_length=30)
    weight: float = Field(le=25, ge=1)
    destination: int | None = Field(
        default_factory=random_destination, ge=1, le=1000000
    )
    status: ShipmentStatus

class ShipmentPatch(BaseModel):
    status: ShipmentStatus
