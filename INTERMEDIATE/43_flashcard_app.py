"""
43: Flashcard App
Implement spaced repetition logic for studying.
"""
cards = [
    {"q": "What is the capital of France?", "a": "Paris"},
    {"q": "What is 2 + 2?", "a": "4"}
]

def review_cards():
    for card in cards:
        ans = input(f"Q: {card['q']} -> ")
        if ans.strip().lower() == card['a'].lower():
            print("Correct!")
        else:
            print(f"Wrong! Answer: {card['a']}")

if __name__ == "__main__":
    print("Flashcard application ready.")
