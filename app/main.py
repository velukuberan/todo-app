from fastapi import FastAPI
from app import models
from app.database import engine

app = FastAPI()

# Auto-create tables (not recommended in production)
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Todo App Backend (Python 3.7) is running!"}
