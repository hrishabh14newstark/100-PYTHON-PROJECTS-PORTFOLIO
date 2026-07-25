"""
05: Hangman Game
A terminal-based word guessing game using string manipulation and loops.
"""
def hangman():
    word = "PYTHON"
    guessed = set()
    tries = 6

    print("--- Hangman Game ---")
    while tries > 0:
        display = "".join([letter if letter in guessed else "_" for letter in word])
        print(f"
Word: {display} | Remaining Tries: {tries}")
        if "_" not in display:
            print("You won!")
            return
        guess = input("Guess a letter: ").upper()
        if guess in guessed:
            print("Already guessed that!")
        elif guess in word:
            guessed.add(guess)
            print("Good guess!")
        else:
            guessed.add(guess)
            tries -= 1
            print("Wrong guess!")
    print(f"Game over! The word was {word}.")

if __name__ == "__main__":
    hangman()
