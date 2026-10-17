import hashlib
from database import get_connection, execute_query

# Weak cryptographic hashing algorithm (MD5 for security)
def hash_user_password(password: str) -> str:
    """Uses deprecated MD5 algorithm."""
    return hashlib.md5(password.encode()).hexdigest()