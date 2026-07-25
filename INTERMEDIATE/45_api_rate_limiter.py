"""
45: API Rate Limiter
Build Python decorators to limit function calls over time.
"""
import time

def rate_limiter(max_calls, period):
    calls = []
    def decorator(func):
        def wrapper(*args, **kwargs):
            now = time.time()
            # keep calls within period
            nonlocal calls
            calls = [c for c in calls if now - c < period]
            if len(calls) >= max_calls:
                raise Exception("Rate limit exceeded! Slow down.")
            calls.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limiter(max_calls=2, period=5)
def fetch_data():
    print("API Data fetched successfully.")

if __name__ == "__main__":
    fetch_data()
    fetch_data()
