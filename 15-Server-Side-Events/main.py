from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import random
import time

app = FastAPI()

# Allow all localhost origins
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Stock price generator
def stock_price_stream():
    price = 100.0
    while True:
        # Generate a random price variation (-1 to +1)
        variation = random.uniform(-1, 1)
        price = max(0, price + variation)  # Ensure price never goes negative
        yield f"data: {{\"price\": {price:.2f}}}\n\n"
        time.sleep(1)  # Update every second

# News generator
news_items = [
    "CHAMPZZ stocks hit a new milestone!",
    "Analysts are optimistic about CHAMPZZ's growth.",
    "Market sees slight volatility; CHAMPZZ holding steady.",
    "Investors rally behind CHAMPZZ's latest announcements."
]

def news_stream():
    while True:
        news = random.choice(news_items)
        yield f"data: {{\"news\": \"{news}\"}}\n\n"
        time.sleep(30)  # Send news every 30 seconds

@app.get("/prices")
async def get_prices():
    return StreamingResponse(stock_price_stream(), media_type="text/event-stream")

@app.get("/news")
async def get_news():
    return StreamingResponse(news_stream(), media_type="text/event-stream")
