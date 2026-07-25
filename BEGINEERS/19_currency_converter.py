"""
19: Currency Converter
Make simple HTTP requests to a free exchange rate API.
"""
import urllib.request
import json

def get_exchange_rate(base="USD", target="EUR"):
    try:
        url = f"https://open.er-api.com/v6/latest/{base}"
        req = urllib.request.urlopen(url)
        data = json.loads(req.read().decode('utf-8'))
        return data['rates'].get(target)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    rate = get_exchange_rate("USD", "EUR")
    print(f"USD to EUR Rate: {rate}")
