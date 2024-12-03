from fastapi import FastAPI
from middlewares import log_requests
from endpoints import users, products, orders
from logger import app_logger

# Initialize FastAPI app
app = FastAPI()

# Middleware
app.middleware("http")(log_requests)

# Routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])

# Root endpoint
@app.get("/")
def read_root():
    app_logger.info("Accessed root endpoint")
    return {"message": "Welcome to the FastAPI app!"}
