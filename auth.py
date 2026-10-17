import hashlib

def hash_user_password(password: str) -> str:
    """Uses SHA256 algorithm for password hashing."""
    return hashlib.sha256(password.encode()).hexdigest()