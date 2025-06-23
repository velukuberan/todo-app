from fastapi import FastAPI
from app.models.item import Item

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Todo App Backend (Python 3.7) is running!"}

@app.get("/items/{item_id}")
def read_items(item_id: int):
    return Item(id=item_id, name="Lord of the Rings", price=2.5)
