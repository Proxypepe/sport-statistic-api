import os


class Config:
    """
    Config class
    """
    DB_USERNAME = os.getenv("DB_USERNAME", "alex")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "32700")
    DB_NAME = os.getenv("DB_NAME", "data")
