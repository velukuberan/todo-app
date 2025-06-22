from fastapi import FastAPI
from app import models
from app.database import engine
from app.models.item import Item

app = FastAPI()

# Auto-create tables (not recommended in production)
# models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Todo App Backend (Python 3.7) is running!"}

@app.get("/items/{item_id}")
def read_items(item_id: int):
    return Item(id=item_id, name="Lord of the Rings", price=2.5)
