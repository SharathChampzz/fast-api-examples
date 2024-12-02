# Rate Limiting Example

## Overview
This example demonstrates how to implement **rate limiting** in a FastAPI application using middleware. Rate limiting controls the number of requests a client can make to the server within a specific time period, improving server performance and preventing abuse.

### Key Concepts
1. **Rate Limiting Middleware**:
   - Tracks client IP addresses and timestamps of their requests.
   - Limits each client to a maximum of 5 requests per minute in this example.

2. **HTTP 429 Response**:
   - If a client exceeds the allowed rate, the server responds with HTTP status code `429 Too Many Requests`.

---

## Features
- Rate limit: **5 requests per minute** per client.
- Middleware tracks requests and enforces limits.

---

## Testing the Rate Limit
1. **Run the Server**:
   - Start the FastAPI application with:
     ```bash
     uvicorn main:app --reload
     ```

2. **Test with the Provided Script**:
   - Use the `test_rate_limit.py` script to verify the rate limit:
     ```bash
     python test_rate_limit.py
     ```

   - Output:
     ```
     Request 1: 200 - {'message': 'Welcome! This endpoint is rate-limited to 5 requests per minute.'}
     ...
     Request 6: 429 - {'detail': 'Rate limit exceeded. Try again later.'}
     Waiting for 60 seconds to reset rate limit...
     Request after cooldown: 200 - {'message': 'Welcome! This endpoint is rate-limited to 5 requests per minute.'}
     ```

3. **Manual Testing**:
   - Use a tool like [Postman](https://www.postman.com) or `curl` to manually send multiple requests and observe the responses.

---

## Notes
- **Custom Limits**:
  - Adjust the `requests_per_minute` parameter in the middleware to set custom limits.

- **Persistent Tracking**:
  - For production, consider integrating a distributed store like Redis to handle rate limits across multiple server instances.
