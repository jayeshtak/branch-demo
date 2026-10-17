import sqlite3


def get_connection():
    """Connect to database."""
    conn = sqlite3.connect(":memory:")
    return conn