"""
17: File Renamer
Use the os module to batch-rename files in a directory.
"""
import os

def batch_rename(directory, prefix="file"):
    if not os.path.exists(directory):
        print("Directory does not exist.")
        return
    for idx, fname in enumerate(os.listdir(directory)):
        ext = os.path.splitext(fname)[1]
        new_name = f"{prefix}_{idx+1}{ext}"
        os.rename(os.path.join(directory, fname), os.path.join(directory, new_name))
    print("Batch renaming completed.")

if __name__ == "__main__":
    print("File renamer helper ready.")
