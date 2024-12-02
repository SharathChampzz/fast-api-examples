# Background Tasks in FastAPI: Sending Emails After Item Addition

## Overview
This example demonstrates how to use **background tasks** in FastAPI to handle non-blocking operations, such as sending emails, after adding an item to a database.

### Key Concepts

1. **Background Tasks**:
   - FastAPI allows scheduling tasks to run in the background while the main API request continues.
   - Useful for operations like sending notifications, processing files, etc.

2. **Simulated Email Sending**:
   - For this example, we simulate an email notification with a print statement.

3. **In-Memory Dummy Database**:
   - A simple Python list (`database.db`) serves as the database for storing item information.

### Features
- **POST /items/**: Add a new item and trigger an email notification in the background.
- **GET /items/**: Retrieve all items from the dummy database.

---

## How It Works
1. When a user adds an item via the `POST /items/` endpoint:
   - The item is stored in the dummy database.
   - A background task is triggered to simulate sending an email notification.
   - The response is returned immediately to the client without waiting for the email task to complete.

2. The `GET /items/` endpoint fetches all items from the dummy database.

---

## Required Modules
Install the following required module for FastAPI:
```bash
pip install fastapi[all]
