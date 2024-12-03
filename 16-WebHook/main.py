from fastapi import FastAPI, Request, HTTPException

app = FastAPI()

@app.post("/webhook")
async def receive_webhook(request: Request):
    # Parse JSON payload
    try:
        payload = await request.json()
        # Process payload (e.g., log or handle event data)
        print("Received webhook payload:", payload)
        return {"status": "success", "message": "Webhook received"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid webhook payload: {str(e)}")
