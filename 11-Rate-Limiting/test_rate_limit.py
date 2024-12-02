# test_rate_limit.py
import requests
import time

URL = "http://127.0.0.1:8000/"  # Adjust to your server's base URL

def test_rate_limiting():
    # Make 5 allowed requests
    for i in range(5):
        response = requests.get(URL)
        print(f"Request {i+1}: {response.status_code} - {response.json()}")

    # 6th request should fail due to rate limiting
    response = requests.get(URL)
    print(f"Request 6: {response.status_code} - {response.json()}")

    # Wait for 1 minute and try again
    print("Waiting for 60 seconds to reset rate limit...")
    time.sleep(60)

    # Make another request after cooldown
    response = requests.get(URL)
    print(f"Request after cooldown: {response.status_code} - {response.json()}")

if __name__ == "__main__":
    test_rate_limiting()
