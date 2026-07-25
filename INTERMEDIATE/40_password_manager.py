"""
40: Password Manager
Secure local storage using cryptography library.
"""
def encrypt_password(plain_text, key):
    try:
        from cryptography.fernet import Fernet
        f = Fernet(key)
        return f.encrypt(plain_text.encode())
    except ImportError:
        return "cryptography package required."

if __name__ == "__main__":
    print("Password manager module ready.")
