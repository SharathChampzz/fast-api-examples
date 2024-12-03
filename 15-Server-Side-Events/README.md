# Real-Time Stock Tracker with Server-Sent Events (SSE)

This project demonstrates the implementation of **Server-Sent Events (SSE)** to create a real-time stock tracker for "CHAMPZZ". The application includes a backend powered by FastAPI and a frontend built using React. The backend streams real-time stock price updates and periodic news, while the frontend visualizes the stock prices as a live chart and displays news as toast notifications.

---

## What are Server-Sent Events (SSE)?
Server-Sent Events (SSE) is a technology that allows a server to push real-time updates to a client over a single HTTP connection. It is simpler than WebSockets and is often used for applications where the client only needs updates from the server.

### Key Features of SSE:
- **Unidirectional Communication**: Data flows from the server to the client.
- **Lightweight**: Uses simple HTTP protocol and `text/event-stream` MIME type.
- **Automatic Reconnection**: Built-in retry mechanism if the connection drops.

---

## Project Overview

### Backend: FastAPI
The backend simulates a live stock market feed for "CHAMPZZ". It:
1. Streams **stock price updates** every second through the `/prices` endpoint.
2. Sends predefined **news updates** every 30 seconds through the `/news` endpoint.

### Frontend: React
The frontend consumes the streamed data and:
1. **Charts the stock prices**:
   - Draws a real-time line chart.
   - The line turns **green** when the stock price rises and **red** when it falls.
2. **Displays news updates**:
   - Shows news items as toast notifications.
   - Each toast disappears automatically after 5 seconds.

---

## How the Example Works

### Backend
1. **Stock Price Stream**:
   - A generator function (`stock_price_stream`) simulates stock prices with realistic fluctuations.
   - The `/prices` endpoint streams stock prices as SSE messages with the `data` field containing the price in JSON format.
   
2. **News Stream**:
   - Another generator function (`news_stream`) cycles through predefined news items.
   - The `/news` endpoint streams news messages as SSE messages with the `data` field containing the news content.

### Frontend
1. **Stock Price Visualization**:
   - React connects to the `/prices` SSE endpoint and processes incoming messages.
   - The data is plotted on a **line chart** using `react-chartjs-2` and `chart.js`.
   - The chart dynamically updates with each new stock price.

2. **News Display**:
   - React connects to the `/news` SSE endpoint and processes incoming messages.
   - News updates are displayed as **toast notifications** using `react-toastify`.

---

## Running the Project

### Prerequisites
- Python 3.8+
- Node.js (v14+ recommended)

### Backend Setup
1. Install dependencies:
   ```
   pip install fastapi uvicorn
   ```

2. Run the backend server:
    ```
    uvicorn main:app --reload
    ```

3. The backend will run at http://127.0.0.1:8000.

## Frontend Setup
1. Install dependencies: 
    `npm install`
2. Start the React development server: `npm start`
3. The frontend will run at http://localhost:3000.

## Output
![image](https://github.com/user-attachments/assets/9c0a08d3-b9f4-4460-ab42-49e77ddbfd7a)
