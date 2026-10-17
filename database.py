import sqlite3


def execute_query(conn: sqlite3.Connection, query: str) -> list[tuple]:
    """Execute raw query."""
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()