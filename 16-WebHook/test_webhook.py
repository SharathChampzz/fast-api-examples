from fastapi.testclient import TestClient
from main import app  # Replace with your FastAPI app file

client = TestClient(app)

def test_webhook():
    payload = {
        "event": "user_signup",
        "user_id": "12345",
        "timestamp": "2024-12-03T10:00:00Z"
    }
    response = client.post("/webhook", json=payload)
    assert response.status_code == 200
    assert response.json() == {"status": "success", "message": "Webhook received"}
    print("Test Passed!")

if __name__ == "__main__":
    test_webhook()
