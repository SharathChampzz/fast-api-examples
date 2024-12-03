from fastapi import APIRouter
from logger import orders_logger

router = APIRouter()

@router.get("/")
def get_orders():
    orders_logger.info("Fetching all orders")
    return {"orders": ["Order 1", "Order 2", "Order 3"]}

@router.get("/{order_id}")
def get_order(order_id: int):
    orders_logger.debug(f"Fetching order with ID: {order_id}")
    if order_id < 0:
        orders_logger.warning(f"Invalid order ID: {order_id}")
        return {"error": "Invalid order ID"}
    return {"order_id": order_id, "details": "Sample Order Details"}
