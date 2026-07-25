"""
88: Spam Email Filter
Train Naive Bayes classifier on text datasets.
"""
def is_spam(text):
    keywords = ["win", "free", "claim", "money", "prize"]
    return any(k in text.lower() for k in keywords)

if __name__ == "__main__":
    print("Is Spam:", is_spam("Claim your free prize now!"))
