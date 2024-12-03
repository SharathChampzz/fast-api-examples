# FastAPI Logging Example (Modular)

This project demonstrates a production-ready approach to logging in a FastAPI application by modularizing the code and using separate loggers for different components.

## How It Works
1. **Centralized Logging Setup:**
   - A `logger.py` file initializes reusable loggers for different components (`app`, `users`, `products`, `orders`).
   - Each logger writes to a dedicated log file (e.g., `users.log` for user-related logs).

2. **Middleware:**
   - A custom middleware logs details about incoming requests, including:
     - HTTP method and URL.
     - Response status code.
     - Time taken to process the request.
   - These logs help monitor the overall application and identify performance bottlenecks.

3. **Component-Specific Logs:**
   - Each endpoint module (e.g., `users`, `products`) logs its operations using its dedicated logger:
     - Example: Fetching all users is logged to `users.log`.
   - This separation improves traceability and simplifies debugging.

4. **Log File Management:**
   - Logs for different components are written to separate files, ensuring that logs remain organized and easy to analyze.
   - File rotation is used to prevent logs from growing indefinitely.

5. **Reusability:**
   - Loggers are imported and reused in multiple modules to ensure consistency in log formatting and configuration.

## How to Use
- Run the application to generate logs for each endpoint in its respective file.
- Analyze specific log files (e.g., `users.log`) to debug or monitor specific parts of the application.

