from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Todo App Backend (Python 3.7) is running!"
    }

@app.get("/shipment")
def get_shipment():
    return {
        "content": "Wooden Table",
        "status": "in transit"
    }

@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API"
    )
