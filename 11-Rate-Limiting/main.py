# main.py
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from time import time
from collections import defaultdict

app = FastAPI()

# Rate limiter middleware
class RateLimiterMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, requests_per_minute: int = 5):
        super().__init__(app)
        self.requests_per_minute = requests_per_minute
        self.clients = defaultdict(list)  # Dictionary to track client requests

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        current_time = time()

        # Clean up old requests older than 1 minute
        self.clients[client_ip] = [
            t for t in self.clients[client_ip] if current_time - t < 60
        ]

        # Check if rate limit is exceeded
        if len(self.clients[client_ip]) >= self.requests_per_minute:
            return JSONResponse(
                {"detail": "Rate limit exceeded. Try again later."},
                status_code=429,
            )

        # Record the request timestamp
        self.clients[client_ip].append(current_time)

        # Continue to the next middleware or endpoint
        return await call_next(request)


# Add the rate limiter middleware to the app
app.add_middleware(RateLimiterMiddleware)

@app.get("/")
async def read_root():
    return {"message": "Welcome! This endpoint is rate-limited to 5 requests per minute."}
