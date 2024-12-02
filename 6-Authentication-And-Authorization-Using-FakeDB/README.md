# FastAPI Authentication and Authorization

This project demonstrates how to implement **authentication** and **authorization** using FastAPI. We utilize JWT (JSON Web Tokens) for secure user login and access control.

---

## **Basic Concepts to Understand the Code**

### **1. Authentication**
Authentication is the process of verifying the identity of a user. In this example, we authenticate the user by validating their username and password against a fake in-memory database.

- **OAuth2PasswordBearer**: This is used to extract the token from the request header. It is part of OAuth2 and allows FastAPI to expect a bearer token for protected routes.
- **OAuth2PasswordRequestForm**: Used to get the username and password from the user when requesting a token.
- **JWT (JSON Web Token)**: A compact and self-contained way to represent information about a user. It is used here to generate an access token that will be sent back to the client.

### **2. Authorization**
Authorization is the process of granting the authenticated user access to specific resources or actions. In this example:
- We protect a route (`/users/me`) that only allows users with a valid JWT token to access it.
- The `Depends(oauth2_scheme)` ensures that the user is authorized to access the route, meaning they must have a valid JWT token.

### **3. JWT Token**
- After successful authentication, the server generates a JWT token using a secret key. This token contains the user's identity (`sub` field) and an expiration time.
- The token is sent to the client, which includes it in the `Authorization` header in subsequent requests to authenticate the user.

### **4. Hashing Passwords**
- Passwords are hashed using **bcrypt** (via the `passlib` library) before storing them in the database. This is to ensure security by not storing plain-text passwords.

---

## **What the Code Does**

- **`/token`**: This is the authentication route where users provide their username and password. If the credentials are valid, the server responds with a JWT token that can be used for subsequent requests.
  
- **`/users/me`**: This is a protected route. Only authenticated users with a valid JWT token can access it. The token is used to verify the user's identity and retrieve user information.

---

This project provides a basic demonstration of how to implement user authentication and authorization in a FastAPI application using JWT tokens.


## Requires:

```pip install passlib PyJWT```