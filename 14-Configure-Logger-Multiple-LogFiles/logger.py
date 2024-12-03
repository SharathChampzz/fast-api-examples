import logging
from logging.handlers import RotatingFileHandler
import os

# Ensure the logs directory exists
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def setup_logger(name, log_file, level=logging.DEBUG):
    """Sets up a logger with a specific file and log level."""
    handler = RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=2)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# Preconfigured loggers for different components
app_logger = setup_logger("app", os.path.join(LOG_DIR, "app.log"))
users_logger = setup_logger("users", os.path.join(LOG_DIR, "users.log"))
products_logger = setup_logger("products", os.path.join(LOG_DIR, "products.log"))
orders_logger = setup_logger("orders", os.path.join(LOG_DIR, "orders.log"))
