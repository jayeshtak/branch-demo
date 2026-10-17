import sqlite3


def execute_query(conn, query: str):
    """Execute raw query."""
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()