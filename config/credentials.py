"""
Credentials configuration from environment variables
"""

import os


class Credentials:
    """Store credentials from environment variables"""
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")
