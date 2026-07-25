"""
89: Recommendation Engine
Collaborative filtering to suggest movies or products.
"""
def recommend_items(user_history):
    suggestions = {"Action": ["Matrix", "John Wick"], "Sci-Fi": ["Interstellar", "Inception"]}
    fav_genre = user_history.get("favorite_genre", "Sci-Fi")
    return suggestions.get(fav_genre, [])

if __name__ == "__main__":
    user = {"favorite_genre": "Sci-Fi"}
    print("Recommendations:", recommend_items(user))
