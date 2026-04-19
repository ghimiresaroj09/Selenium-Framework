"""
Logger utility for Selenium Framework
"""

import logging
import os
from logging.handlers import RotatingFileHandler
from config import TestConfig


def get_logger(name):

    if not os.path.exists(TestConfig.LOGS_PATH):
        os.makedirs(TestConfig.LOGS_PATH)

    logger = logging.getLogger(name)

    if logger.hasHandlers():
        return logger

    # Convert string level → logging level
    level = getattr(logging, TestConfig.LOG_LEVEL.upper(), logging.INFO)

    logger.setLevel(level)
    logger.propagate = False

    log_file = os.path.join(TestConfig.LOGS_PATH, "selenium_tests.log")

    # File handler with rotation
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=5 * 1024 * 1024,
        backupCount=3
    )
    file_handler.setLevel(level)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # Formatter
    formatter = logging.Formatter(TestConfig.LOG_FORMAT)
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger