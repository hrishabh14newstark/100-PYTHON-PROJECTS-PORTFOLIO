"""
82: Distributed Task Queue
Build a miniature version of Celery using Redis.
"""
import queue

task_q = queue.Queue()

def enqueue_task(func_name, *args):
    task_q.put((func_name, args))
    print(f"Task '{func_name}' queued.")

if __name__ == "__main__":
    enqueue_task("send_welcome_email", "user@test.com")
