# FastAPI Webhook Example

## Overview

This project demonstrates how to implement and test a webhook using FastAPI. Webhooks are a mechanism for real-time communication between applications, enabling event-driven notifications without the need for constant polling.

---

## What Are Webhooks?

Webhooks are **event-driven HTTP callbacks** that allow one application to send data to another application whenever a specific event occurs. They are widely used in modern software systems for real-time event notifications.

### How Are Webhooks Different from APIs?

| Feature            | API (Polling)                                         | Webhooks                                              |
|---------------------|-------------------------------------------------------|-------------------------------------------------------|
| **Communication**  | Client actively requests data at intervals.           | Server sends data to the client automatically on events. |
| **Efficiency**     | Resource-intensive due to repeated requests.          | Lightweight, sends data only when an event occurs.    |
| **Real-Time**      | Delayed updates depending on polling intervals.        | Instant updates triggered by the event.              |
| **Usage**          | Better for retrieving large datasets or on-demand data. | Ideal for notifying applications of event changes.   |

---

### Why Do We Need Webhooks?

APIs require constant polling to check for updates, which is inefficient and increases latency. Webhooks, on the other hand, eliminate this by pushing data immediately when an event occurs.

---

### Example: Understanding Webhooks

Imagine you're ordering food delivery:  
- **Using APIs:** You constantly call the restaurant asking, "Is my food ready yet?" (polling).  
- **Using Webhooks:** The restaurant calls you when your food is ready (event-driven).

With webhooks, the restaurant notifies you the moment your food is prepared, saving time and effort on both sides.

---

## How This Project Works

### Code Structure

1. **`webhook_app.py`:**  
   Implements a FastAPI application to receive and handle webhooks. The `/webhook` endpoint listens for `POST` requests and processes incoming JSON payloads.

2. **`send_webhook.py`:**  
   Simulates an external service sending a webhook request. This script helps test the webhook receiver by sending JSON payloads to the FastAPI endpoint.

3. **`test_webhook.py`:**  
   Contains automated tests using FastAPI's `TestClient`. This validates that the webhook endpoint behaves as expected when receiving payloads.

---

## Workflow

1. The FastAPI application sets up a listener on the `/webhook` endpoint.
2. External services send an HTTP `POST` request to the `/webhook` endpoint with event data in JSON format.
3. The application processes and logs the data, responding with a success message.
4. Test scripts ensure that the implementation handles data correctly.

---


