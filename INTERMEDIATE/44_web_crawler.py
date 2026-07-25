"""
44: Web Crawler
Recursively index links and text of a small website.
"""
import urllib.request
import re

def crawl(start_url, max_pages=3):
    visited = set()
    to_visit = [start_url]

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop(0)
        if url in visited: continue
        visited.add(url)
        print(f"Crawling: {url}")

if __name__ == "__main__":
    crawl("https://example.com")
