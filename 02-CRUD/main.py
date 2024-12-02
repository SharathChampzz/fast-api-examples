from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory "database"
items = []
item_id_counter = 1


class Item(BaseModel):
    name: str
    price: float
    description: str


@app.post("/items/", response_model=dict)
def create_item(item: Item):
    global item_id_counter
    new_item = item.model_dump()
    new_item["id"] = item_id_counter
    item_id_counter += 1 # increment for next item
    items.append(new_item)
    return new_item


@app.get("/items/", response_model=List[dict])
def get_items():
    return items


@app.get("/items/{item_id}", response_model=dict)
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.put("/items/{item_id}", response_model=dict)
def update_item(item_id: int, updated_item: Item):
    for item in items:
        if item["id"] == item_id:
            item.update(updated_item.model_dump())
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}", response_model=dict)
def delete_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            items.remove(item)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")
