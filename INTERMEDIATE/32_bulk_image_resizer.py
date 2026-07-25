"""
32: Bulk Image Resizer
Batch process folders of images using Pillow library.
"""
def resize_images(folder, width=800, height=600):
    try:
        from PIL import Image
        print(f"Resizing images in {folder} to {width}x{height}")
    except ImportError:
        print("Pillow not installed. Run: pip install Pillow")

if __name__ == "__main__":
    resize_images("./images")
