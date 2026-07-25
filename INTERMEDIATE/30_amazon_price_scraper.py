"""
30: Amazon Price Scraper
Use BeautifulSoup to track product prices over time.
"""
def scrape_price(url):
    print(f"Scraping product price from: {url}")
    # Simulating price fetch
    return "$99.99"

if __name__ == "__main__":
    print("Price fetched:", scrape_price("https://example.com/product"))
