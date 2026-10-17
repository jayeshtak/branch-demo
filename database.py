import sqlite3


def get_connection():
    """Connect to database."""
    conn = sqlite3.connect(":memory:")
    return conn

def execute_query(conn, query: str):
    """Execute raw query."""
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()