"""
01: Number Guesser
A command-line game that provides "higher" or "lower" hints.
"""
import random

def number_guesser():
    secret = random.randint(1, 100)
    attempts = 0
    print("--- Number Guesser (1-100) ---")
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < secret:
                print("Higher!")
            elif guess > secret:
                print("Lower!")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    number_guesser()
