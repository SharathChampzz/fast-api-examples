from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import hashlib
import time

app = FastAPI()

# In-memory storage for simplicity
url_mapping = {}

class URLRequest(BaseModel):
    long_url: str
    custom_alias: Optional[str] = None
    expires_in: Optional[int] = None  # Expiration time in seconds

@app.post("/shorten")
def shorten_url(request: URLRequest):
    if request.custom_alias:
        short_url = request.custom_alias
    else:
        short_url = hashlib.md5(request.long_url.encode()).hexdigest()[:6]
    
    if short_url in url_mapping:
        raise HTTPException(status_code=400, detail="Short URL already exists")
    
    expires_at = time.time() + request.expires_in if request.expires_in else None
    url_mapping[short_url] = {"long_url": request.long_url, "expires_at": expires_at}
    
    return {"short_url": short_url}

@app.get("/{short_url}")
def redirect(short_url: str):
    if short_url not in url_mapping:
        raise HTTPException(status_code=404, detail="Short URL not found")
    
    entry = url_mapping[short_url]
    if entry["expires_at"] and time.time() > entry["expires_at"]:
        del url_mapping[short_url]
        raise HTTPException(status_code=404, detail="Short URL expired")
    
    return {"long_url": entry["long_url"]}
