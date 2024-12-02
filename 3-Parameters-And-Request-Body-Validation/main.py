from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

# In-memory database
items = []

# Models
class Item(BaseModel):
    name: str
    price: float
    description: str = "No description provided"

class ItemWithValidation(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    price: float = Field(gt=0, lt=10000, description="Price must be between 0 and 10,000")
    description: str = Field(default="No description provided", max_length=200)


# Path Parameters
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


# Query Parameters
@app.get("/search/")
def search_items(q: Optional[str] = None, limit: int = 10):
    return {"query": q, "limit": limit}


# JSON Request Body
@app.post("/items/")
def create_item(item: Item):
    item_id = len(items) + 1
    items.append({"id": item_id, **item.model_dump()})
    return {"id": item_id, **item.model_dump()}


# Validation with Pydantic
@app.post("/validated-items/")
def create_validated_item(item: ItemWithValidation):
    return {"name": item.name, "price": item.price, "description": item.description}


# Combine Path, Query Parameters, and JSON Body
@app.get("/items/{item_id}/")
def get_item_with_query(item_id: int, detail: bool = False):
    return {"item_id": item_id, "detail": detail}


@app.put("/items/{item_id}/")
def update_item(item_id: int, item: Item):
    for db_item in items:
        if db_item["id"] == item_id:
            db_item.update(item.dict())
            return db_item
    raise HTTPException(status_code=404, detail="Item not found")
