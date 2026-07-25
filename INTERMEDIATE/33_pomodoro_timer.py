"""
33: Pomodoro Timer
A GUI productivity app with work/rest intervals.
"""
import time

def pomodoro(work_mins=25, break_mins=5):
    print(f"Work session started for {work_mins} minutes...")
    # time.sleep(work_mins * 60)
    print(f"Take a break for {break_mins} minutes!")

if __name__ == "__main__":
    pomodoro(25, 5)
