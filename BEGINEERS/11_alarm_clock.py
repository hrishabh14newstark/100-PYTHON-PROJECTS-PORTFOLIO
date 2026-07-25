"""
11: Alarm Clock
Schedule a print statement or sound at a specific time.
"""
import datetime
import time

def set_alarm(target_time_str):
    print(f"Alarm set for {target_time_str}")
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == target_time_str:
            print("
[ALARM] Wake up! Time reached!")
            break
        time.sleep(1)

if __name__ == "__main__":
    print("Alarm clock script loaded.")
