"""
25: Caesar Cipher
Create a simple text encryption and decryption tool.
"""
def caesar_cipher(text, shift, mode='encrypt'):
    if mode == 'decrypt':
        shift = -shift
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

if __name__ == "__main__":
    encrypted = caesar_cipher("Hello World", 3, 'encrypt')
    print("Encrypted:", encrypted)
    print("Decrypted:", caesar_cipher(encrypted, 3, 'decrypt'))
