from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Step 1: Define Item model
# This represents a single item in an order
class Item(BaseModel):
    name: str
    price: float
    quantity: int

# Step 2: Define Order model
# This represents an order with a list of items
class Order(BaseModel):
    order_id: int
    customer_name: str
    items: List[Item]  # List of items in the order

# Step 3: Define a response model for a summary of an order
class OrderSummary(BaseModel):
    order_id: int
    customer_name: str
    total_price: float

# Step 4: Define Custom Error
# A custom exception handler that returns a friendly error message
class ItemNotFoundError(HTTPException):
    def __init__(self, item_name: str):
        self.status_code = 404
        self.detail = f"Item '{item_name}' not found in the order."

# In-memory database (just for the purpose of this example)
orders_db = {}

# Step 5: Create API Endpoints
@app.post("/orders/", response_model=OrderSummary)
def create_order(order: Order):
    # Calculate total price
    total_price = sum(item.price * item.quantity for item in order.items)
    
    # Save order to "database"
    orders_db[order.order_id] = order
    
    # Return order summary (response model)
    return OrderSummary(order_id=order.order_id, customer_name=order.customer_name, total_price=total_price)

@app.get("/orders/{order_id}", response_model=Order)
def get_order(order_id: int):
    # Check if the order exists in the database
    if order_id not in orders_db:
        raise HTTPException(status_code=404, detail="Order not found")
    
    # Return the order from the database
    return orders_db[order_id]

@app.delete("/orders/{order_id}", response_model=dict)
def delete_order(order_id: int):
    # Check if the order exists
    if order_id not in orders_db:
        raise ItemNotFoundError(item_name=str(order_id))
    
    # Delete the order from the database
    del orders_db[order_id]
    
    return {"message": "Order deleted successfully"}

@app.get("/orders/{order_id}/item/{item_name}")
def get_item_from_order(order_id: int, item_name: str):
    # Get the order
    order = orders_db.get(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    # Check if the item exists in the order
    item = next((item for item in order.items if item.name == item_name), None)
    if not item:
        raise ItemNotFoundError(item_name=item_name)
    
    # Return the found item
    return item
