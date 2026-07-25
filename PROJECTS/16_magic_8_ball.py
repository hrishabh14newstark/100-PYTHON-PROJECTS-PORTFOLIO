"""
16: Magic 8-Ball
Return randomized responses to user questions.
"""
import random

RESPONSES = [
    "It is certain.", "Reply hazy, try again.", "Don't count on it.",
    "Outlook good.", "Signs point to yes.", "Very doubtful."
]

def magic_8_ball():
    input("Ask a yes/no question: ")
    print("Magic 8-Ball says:", random.choice(RESPONSES))

if __name__ == "__main__":
    magic_8_ball()
