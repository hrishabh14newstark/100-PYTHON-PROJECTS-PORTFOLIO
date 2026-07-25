"""
39: Typing Speed Tester
Measure words-per-minute via a terminal interface.
"""
import time

def typing_test():
    prompt = "The quick brown fox jumps over the lazy dog"
    print("Type this sentence as fast as you can:
")
    print(f"'{prompt}'
")
    input("Press Enter when ready...")
    start = time.time()
    typed = input("
Type here: ")
    end = time.time()

    elapsed = end - start
    words = len(typed.split())
    wpm = (words / elapsed) * 60
    print(f"
Time: {elapsed:.2f}s | WPM: {wpm:.1f}")

if __name__ == "__main__":
    print("Typing tester module loaded.")
