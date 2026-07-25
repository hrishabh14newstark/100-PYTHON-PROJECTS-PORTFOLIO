"""
10: Countdown Timer
A terminal timer utilizing the time module.
"""
import time

def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="")
        time.sleep(1)
        seconds -= 1
    print("
Time's up!")

if __name__ == "__main__":
    countdown(3)
