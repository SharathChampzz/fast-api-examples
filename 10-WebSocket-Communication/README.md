# WebSocket Communication Example

## Overview
This example demonstrates how to use WebSockets with FastAPI for real-time, two-way communication between the server and clients.

### Key Concepts
1. **WebSocket Protocol**:
   - WebSockets enable persistent, full-duplex communication channels between the client and server.
   - Useful for applications like chat systems, real-time notifications, and live updates.

2. **Connection Manager**:
   - A helper class (`ConnectionManager`) manages active WebSocket connections.
   - Supports broadcasting messages to all connected clients.

3. **Broadcasting Messages**:
   - The server broadcasts messages received from one client to all connected clients.

---

## Features
- **WebSocket Endpoint**:
  - Endpoint: `/ws`
  - Clients can connect, send messages, and receive real-time responses.

---

## Example Workflow
1. **Connect to the WebSocket Server**:
   - Use tools like [WebSocket King](https://websocketking.com) or browser developer tools to connect to `ws://<server-url>/ws` , example: `ws://localhost:8000/ws`.

2. **Send a Message**:
   - After connecting, send a text message through the WebSocket.
   - Example message: `Hello, WebSocket!`

3. **Receive Broadcast**:
   - All connected clients, including the sender, will receive the message:
     ```
     Client says: Hello, WebSocket!
     ```

---

## Notes
- **WebSocket Connection**:
  - WebSocket URLs use the `ws://` or `wss://` scheme (for unencrypted and encrypted connections, respectively).

- **Broadcasting**:
  - The server broadcasts messages to all connected clients.

- **Customization**:
  - Extend the `ConnectionManager` to support private messaging, message history, or advanced features as needed.
