import requests

url = "http://127.0.0.1:8000/webhook"  # Replace with your webhook URL
payload = {
    "event": "user_signup",
    "user_id": "12345",
    "timestamp": "2024-12-03T10:00:00Z"
}

response = requests.post(url, json=payload)
print("Response Status Code:", response.status_code)
print("Response Body:", response.json())
