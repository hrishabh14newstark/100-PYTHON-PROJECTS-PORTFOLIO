"""
12: Word Counter
Parse text files to count frequency of words using dictionaries.
"""
from collections import Counter

def count_words(text):
    words = text.lower().split()
    return Counter(words)

if __name__ == "__main__":
    sample_text = "Python is great and Python is easy to learn."
    counts = count_words(sample_text)
    print("Word Frequencies:", counts)
