"""
07: To-Do List (CLI)
Manage tasks using basic text file read/write operations.
"""
import os

FILENAME = "tasks.txt"

def add_task(task):
    with open(FILENAME, "a") as f:
        f.write(task + "
")

def view_tasks():
    if not os.path.exists(FILENAME):
        print("No tasks found.")
        return
    with open(FILENAME, "r") as f:
        tasks = f.readlines()
    print("
Tasks:")
    for idx, t in enumerate(tasks, 1):
        print(f"{idx}. {t.strip()}")

if __name__ == "__main__":
    add_task("Sample Task")
    view_tasks()
