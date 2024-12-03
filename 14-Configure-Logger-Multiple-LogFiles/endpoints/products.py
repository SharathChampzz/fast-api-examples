from fastapi import APIRouter
from logger import products_logger

router = APIRouter()

@router.get("/")
def get_products():
    products_logger.info("Fetching all products")
    return {"products": ["Product A", "Product B", "Product C"]}

@router.get("/{product_id}")
def get_product(product_id: int):
    products_logger.debug(f"Fetching product with ID: {product_id}")
    if product_id < 0:
        products_logger.warning(f"Invalid product ID: {product_id}")
        return {"error": "Invalid product ID"}
    return {"product_id": product_id, "name": "Sample Product"}
