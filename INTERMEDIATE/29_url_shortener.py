"""
29: URL Shortener
A web app that hashes long links into short redirects.
"""
import hashlib

url_db = {}

def shorten_url(long_url):
    short_hash = hashlib.md5(long_url.encode()).hexdigest()[:6]
    url_db[short_hash] = long_url
    return f"http://short.ly/{short_hash}"

if __name__ == "__main__":
    short = shorten_url("https://www.example.com/very/long/url/path")
    print("Shortened URL:", short)
