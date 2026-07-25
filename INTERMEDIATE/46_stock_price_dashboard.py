"""
46: Stock Price Dashboard
Pull and graph financial data from public APIs.
"""
def fetch_stock(symbol="AAPL"):
    print(f"Fetching financial data for {symbol}...")
    return [150.2, 151.5, 153.0, 152.8]

if __name__ == "__main__":
    data = fetch_stock()
    print("Recent prices:", data)
