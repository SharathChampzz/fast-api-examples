from fastapi import Request
from logger import app_logger
import time

async def log_requests(request: Request, call_next):
    """Logs incoming requests and response times."""
    start_time = time.time()

    # Log request details
    app_logger.info(f"Received request: {request.method} {request.url}")

    response = await call_next(request)

    # Log response details
    process_time = time.time() - start_time
    app_logger.info(f"Response status: {response.status_code}, Time: {process_time:.2f}s")

    return response
