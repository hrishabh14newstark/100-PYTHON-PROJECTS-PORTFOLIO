"""
03: Password Generator
Generate secure, random passwords using the secrets module.
"""
import secrets
import string

def generate_password(length=16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Generated Secure Password:", generate_password(16))
