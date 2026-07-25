"""
23: Wikipedia Fetcher
Retrieve and summarize random articles using Wikipedia API.
"""
import urllib.request
import json

def fetch_random_wiki_summary():
    url = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'PythonWikiApp/1.0'})
        res = urllib.request.urlopen(req)
        data = json.loads(res.read().decode('utf-8'))
        return data.get('title'), data.get('extract')
    except Exception as e:
        return "Error", str(e)

if __name__ == "__main__":
    title, extract = fetch_random_wiki_summary()
    print(f"Title: {title}
Summary: {extract}")
