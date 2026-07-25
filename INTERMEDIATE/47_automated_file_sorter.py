"""
47: Automated File Sorter
Organize a cluttered folder by file extension.
"""
import os
import shutil

EXTENSION_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Code": [".py", ".cpp", ".html"]
}

def sort_folder(folder_path):
    if not os.path.exists(folder_path): return
    for f in os.listdir(folder_path):
        ext = os.path.splitext(f)[1].lower()
        for category, exts in EXTENSION_MAP.items():
            if ext in exts:
                target_dir = os.path.join(folder_path, category)
                os.makedirs(target_dir, exist_ok=True)
                shutil.move(os.path.join(folder_path, f), os.path.join(target_dir, f))

if __name__ == "__main__":
    print("File sorter utility script ready.")
