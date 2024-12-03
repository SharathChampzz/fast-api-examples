import logging
from fastapi import FastAPI, HTTPException
import users

# Create FastAPI app
app = FastAPI()
app.include_router(users.router, prefix="/users", tags=["Users"])

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Minimum log level for the application
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  # Logs to console
        logging.FileHandler("app.log"),  # Logs to a file
    ],
)

# Get a logger instance
logger = logging.getLogger("fastapi_app")


@app.get("/")
def read_root():
    logger.debug("Debug: Accessing the root endpoint")
    logger.info("Info: Root endpoint accessed successfully")
    return {"message": "Welcome to the FastAPI app!"}


@app.get("/item/{item_id}")
def read_item(item_id: int):
    logger.debug(f"Debug: Received request for item {item_id}")
    if item_id < 0:
        logger.warning(f"Warning: Negative item ID {item_id} received")
        raise HTTPException(status_code=400, detail="Invalid item ID")
    logger.info(f"Info: Returning item with ID {item_id}")
    return {"item_id": item_id}


@app.get("/error")
def trigger_error():
    try:
        logger.debug("Debug: About to trigger an error")
        raise ValueError("A sample error occurred!")
    except ValueError as e:
        logger.error(f"Error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal Server Error")
