import hashlib

def hash_password_sha256(password: str, salt: str) -> str:
    return hashlib.sha256((salt + password).encode()).hexdigest()

# Example usage
salt = "random_salt_123"
password = "password123"
hashed = hash_password_sha256(password, salt)
print("SHA-256 Hash:", hashed)
