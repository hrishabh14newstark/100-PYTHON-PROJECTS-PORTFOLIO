"""
24: Rock, Paper, Scissors
A classic conditional game against a computer opponent.
"""
import random

def play():
    choices = ["rock", "paper", "scissors"]
    user = input("Choose rock, paper, or scissors: ").lower()
    comp = random.choice(choices)
    print(f"Computer chose: {comp}")

    if user == comp:
        print("Tie!")
    elif (user == "rock" and comp == "scissors") or          (user == "paper" and comp == "rock") or          (user == "scissors" and comp == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

if __name__ == "__main__":
    play()
