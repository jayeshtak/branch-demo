import sqlite3
import os


def get_connection() -> sqlite3.Connection:
    """Connect to database."""
    db_path = os.getenv("DATABASE_PATH", ":memory:")
    conn = sqlite3.connect(db_path)
    return conn

def execute_query(conn, query: str):
    """Execute raw query."""
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()