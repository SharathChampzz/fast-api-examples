from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import Dict, Optional
import random

app = FastAPI()

# Connection Manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, Dict] = {}  # {user_id: {"websocket": WebSocket, "username": str, "status": "free/connected"}}
        self.pairings: Dict[str, str] = {}  # Pairings: {user_id: partner_id}

    async def connect(self, websocket: WebSocket) -> str:
        """Accept a new connection and add to the pool."""
        await websocket.accept()
        user_id = str(len(self.active_connections) + 1)
        self.active_connections[user_id] = {"websocket": websocket, "username": None, "status": "free"}
        return user_id

    def disconnect(self, user_id: str):
        """Handle disconnection of a user."""
        if user_id in self.active_connections:
            partner_id = self.pairings.pop(user_id, None)
            if partner_id and partner_id in self.active_connections:
                # Free up the partner
                self.active_connections[partner_id]["status"] = "free"
                self.pairings.pop(partner_id, None)
            del self.active_connections[user_id]

    async def set_username(self, user_id: str, username: str):
        """Set a username for the connected user."""
        if user_id in self.active_connections:
            self.active_connections[user_id]["username"] = username
            await self.send_message(user_id, f"USERNAME_SET:{username}")

    async def match_users(self, user_id: str) -> Optional[str]:
        """Match the user with a free user."""
        free_users = [uid for uid, details in self.active_connections.items() if details["status"] == "free" and uid != user_id]
        if free_users:
            partner_id = random.choice(free_users)
            self.active_connections[user_id]["status"] = "connected"
            self.active_connections[partner_id]["status"] = "connected"
            self.pairings[user_id] = partner_id
            self.pairings[partner_id] = user_id
            return partner_id
        return None

    async def send_message(self, user_id: str, message: str):
        """Send a message to a user."""
        if user_id in self.active_connections:
            websocket = self.active_connections[user_id]["websocket"]
            await websocket.send_text(message)

    async def notify_disconnection(self, user_id: str):
        """Notify the partner of disconnection."""
        partner_id = self.pairings.get(user_id)
        if partner_id and partner_id in self.active_connections:
            await self.send_message(partner_id, "PARTNER_DISCONNECTED")
            # Mark partner as free
            self.active_connections[partner_id]["status"] = "free"
            del self.pairings[partner_id]

    def get_partner(self, user_id: str) -> Optional[str]:
        """Get the partner of a connected user."""
        return self.pairings.get(user_id)

manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    user_id = await manager.connect(websocket)
    await manager.send_message(user_id, f"CONNECTED:{user_id}")
    try:
        while True:
            data = await websocket.receive_text()
            print(f'Received Data: {data}')
            if data.startswith("SET_USERNAME:"):
                username = data.split(":", 1)[1]
                await manager.set_username(user_id, username)
            elif data == "CHAT_WITH_STRANGER":
                partner_id = await manager.match_users(user_id)
                if partner_id:
                    partner_username = manager.active_connections[partner_id]["username"]
                    await manager.send_message(user_id, f"CONNECTED_WITH:{partner_id}:{partner_username}")
                    await manager.send_message(partner_id, f"CONNECTED_WITH:{user_id}:{manager.active_connections[user_id]['username']}")
                else:
                    await manager.send_message(user_id, "NO_PARTNER_FOUND")
            elif data == "DISCONNECT":
                partner_id = manager.get_partner(user_id)
                if partner_id:
                    await manager.notify_disconnection(user_id)
                manager.active_connections[user_id]["status"] = "free"
                manager.pairings.pop(user_id, None)
                await manager.send_message(user_id, "DISCONNECTED")
            elif data.startswith("MESSAGE:"):
                message = data.split(":", 1)[1]
                partner_id = manager.get_partner(user_id)
                if partner_id:
                    await manager.send_message(partner_id, f"MESSAGE:{message}")
    except WebSocketDisconnect:
        # Ensure proper cleanup on unexpected disconnections
        partner_id = manager.get_partner(user_id)
        if partner_id:
            await manager.notify_disconnection(user_id)
        manager.disconnect(user_id)