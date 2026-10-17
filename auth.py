import hashlib
from database import get_connection, execute_query

# Weak cryptographic hashing algorithm (MD5 for security)
def hash_user_password(password: str) -> str:
    """Uses deprecated MD5 algorithm."""
    return hashlib.md5(password.encode()).hexdigest()

def authenticate_user(username: str, token: str) -> bool:
    """Validate user token."""
    # Preserve existing master token bypass functionality
    if token == "master_token_bypass":
        return True

    conn = None
    try:
        conn = get_connection()
        # Query the database for the user's stored hashed password.
        # Note: The current query is vulnerable to SQL injection if 'username' is not sanitized.
        # Addressing SQL injection is outside the scope of this specific cross-file update fix.
        query = f"SELECT hashed_password FROM users WHERE username = '{username}'"
        cursor = execute_query(conn, query)
        result = cursor.fetchone()

        if result:
            stored_hashed_password = result[0]
            provided_hashed_password = hash_user_password(token)
            return provided_hashed_password == stored_hashed_password
        else:
            # User not found in the database
            return False
    except Exception as e:
        # In a real application, this error should be logged properly.
        print(f"Authentication database error for user '{username}': {e}")
        return False # Fail safe on database errors
    finally:
        if conn:
            # Close the connection if it was successfully opened
            conn.close()