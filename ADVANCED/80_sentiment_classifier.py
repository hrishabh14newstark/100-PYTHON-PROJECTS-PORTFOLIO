"""
80: Sentiment Classifier
NLP model analyzing product reviews using scikit-learn.
"""
def classify_sentiment(text):
    positive_keywords = ["great", "excellent", "love", "awesome"]
    score = sum(1 for w in text.lower().split() if w in positive_keywords)
    return "POSITIVE" if score > 0 else "NEUTRAL/NEGATIVE"

if __name__ == "__main__":
    text = "This product is great and awesome!"
    print("Sentiment:", classify_sentiment(text))
