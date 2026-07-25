"""
18: Directory Scanner
Traverse folders to list file types and calculate sizes.
"""
import os

def scan_directory(path="."):
    total_size = 0
    file_count = 0
    for root, _, files in os.walk(path):
        for f in files:
            fp = os.path.join(root, f)
            total_size += os.path.getsize(fp)
            file_count += 1
    return file_count, total_size

if __name__ == "__main__":
    count, size = scan_directory(".")
    print(f"Scanned directory: {count} files, Total size: {size / 1024:.2f} KB")
