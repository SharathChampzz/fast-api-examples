# main.py
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List

app = FastAPI()

# Manager to handle connected clients
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        print("Request received for websocket connection...")
        await websocket.accept()
        self.active_connections.append(websocket)
        print('Added new connection!')

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        print('Removed new connection!')

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)
            print(f"Broadcasted message : {message}!!")


manager = ConnectionManager()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Client says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
