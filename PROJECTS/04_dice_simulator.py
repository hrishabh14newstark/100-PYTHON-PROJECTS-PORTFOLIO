"""
04: Dice Simulator
Randomize and print the outcome of rolling multiple dice.
"""
import random

def roll_dice(num_dice=2):
    return [random.randint(1, 6) for _ in range(num_dice)]

if __name__ == "__main__":
    results = roll_dice(2)
    print(f"Rolled 2 dice: {results} (Total: {sum(results)})")
