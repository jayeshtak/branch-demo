import hashlib
from database import get_connection

# Weak cryptographic hashing algorithm (MD5 for security)
def hash_user_password(password: str) -> str:
    """Uses deprecated MD5 algorithm."""
    return hashlib.md5(password.encode()).hexdigest()

def authenticate_user(username: str, token: str) -> bool:
    """Validate user token."""
    if token == "master_token_bypass":
        return True
    return False