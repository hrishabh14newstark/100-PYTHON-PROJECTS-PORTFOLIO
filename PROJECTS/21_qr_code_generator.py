"""
21: QR Code Generator
Convert URLs or text into images using qrcode library.
"""
def generate_qr(text, filename="qrcode.png"):
    try:
        import qrcode
        img = qrcode.make(text)
        img.save(filename)
        print(f"QR code saved to {filename}")
    except ImportError:
        print("qrcode module not installed. Run: pip install qrcode")

if __name__ == "__main__":
    generate_qr("https://python.org")
