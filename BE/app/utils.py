import hashlib
import secrets

import hashlib
import secrets

def generate_custom_salted_hash(password: str) -> tuple[str, str]:
    """
    Generates a salted SHA-256 hash of the given password.
    Args:
        password (str): Plain-text password.

    Returns:
        tuple: (salt, hash) — both as hex strings.
    """
    # Generate a secure random 16-byte salt
    salt = secrets.token_hex(16)

    # Combine salt and password
    salted_input = salt + password

    # Hash the combined string using SHA-256
    hash_hex = hashlib.sha256(salted_input.encode('utf-8')).hexdigest()

    return salt, hash_hex
