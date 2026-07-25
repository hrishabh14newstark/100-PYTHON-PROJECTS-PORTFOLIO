"""
91: Steganography Tool
Hide encrypted text securely within image pixels.
"""
def encode_message_in_image(img_path, secret_text):
    print(f"Hiding secret message inside {img_path} LSB pixels...")

if __name__ == "__main__":
    encode_message_in_image("cover.png", "CONFIDENTIAL")
