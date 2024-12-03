# Omegle Lite

Omegle Lite is a simplified web application that allows users to chat with random strangers. Built using **FastAPI** for the backend and a minimalistic frontend with HTML, CSS, and JavaScript, it demonstrates real-time WebSocket communication and dynamic user pairing.

## Features
- Connect with random strangers for one-on-one chats.
- Disconnection handling with notifications.
- User-friendly UI with a responsive design for both mobile and desktop devices.
- Real-time communication powered by WebSockets.
- Username-based identity for testing multiple clients on the same device.

## How It Works

### Backend (FastAPI)
1. **WebSocket Management:**
   - Each user establishes a WebSocket connection on page load.
   - A unique `user_id` is assigned to every connection and stored in an active connections list.

2. **Username Setup:**
   - Users provide their username on initial connection, which is stored alongside their WebSocket details.

3. **User Matching:**
   - When a user clicks "Chat with Stranger," the backend finds another free user from the pool of connected clients.
   - If a match is found, both users are notified of their pairing and can exchange messages.

4. **Message Handling:**
   - Messages are tagged with the sender’s `user_id` and forwarded to the intended recipient.

5. **Disconnection Handling:**
   - When a user disconnects, their partner is notified with a "Partner Disconnected" message.
   - Both users are returned to the free pool, and their chat states are reset.

### Frontend
1. **Username Input:**
   - A popup asks for the username upon page load.
   - After entering the username, a WebSocket connection is established with the backend.

2. **Chat Functionality:**
   - Users can click "Chat with Stranger" to get paired with a random free user.
   - Messages typed in the input field are sent to the server and forwarded to the connected user.

3. **UI Notifications:**
   - Users are notified when their partner disconnects.
   - Users can disconnect manually and start a new chat with another stranger.

4. **Responsive Design:**
   - Optimized for both mobile and desktop devices.
   - Message bubbles and controls are styled for a clean, modern appearance.

Output Screenshot:

User 1: "Champzz"

![image](https://github.com/user-attachments/assets/b41c2aee-c31e-4ce7-9777-8b7ef875305b)

User 2: "Sharath"

![image](https://github.com/user-attachments/assets/c38f54eb-d0da-4aac-8b77-9d44fe6f415a)

