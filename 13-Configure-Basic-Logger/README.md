# FastAPI Logging Example (Single-File)

This project demonstrates a straightforward way to implement logging in a FastAPI application. All the logic, including logging setup, is contained within a single file (`main.py`).

## How It Works
1. **Logging Setup:**
   - Python's built-in `logging` module is configured using `logging.basicConfig` to log messages both to the console and a file (`app.log`).
   - Logs include details such as timestamps, log levels, and messages.

2. **Log Levels:**
   - The application uses various log levels (e.g., DEBUG, INFO, WARNING, ERROR) to demonstrate their usage:
     - `INFO`: Logs successful access to endpoints.
     - `DEBUG`: Logs detailed information about requests.
     - `WARNING`: Logs potential issues, such as invalid inputs.

3. **Endpoint Logging:**
   - Each endpoint in the application logs relevant details:
     - Root endpoint logs an informational message when accessed.
     - Other endpoints log details about user requests, potential errors, and warnings.

4. **Log File Rotation:**
   - The log file (`app.log`) uses a `RotatingFileHandler` to limit its size and maintain a maximum of 2 backup files.

5. **Module logger**
    - By using `getLogger(__name__)`, you create a logger for individual modules to separate the logs. This will ensure that log lines include the module name in the log files
    ```
    import logging
    logger = logging.getLogger("fastapi_app")
    users_logger = logging.getLogger(__name__) # users module
    ```
    ```
    2024-12-03 12:16:44,384 - fastapi_app - INFO - Info: Returning item with ID 34
    2024-12-03 12:19:26,570 - users - INFO - Fetching all users
    ```


## How to Use
- When you run the application, all log messages are written to both the console and the `app.log` file.
- This setup is ideal for small applications or as a starting point to learn logging basics.

