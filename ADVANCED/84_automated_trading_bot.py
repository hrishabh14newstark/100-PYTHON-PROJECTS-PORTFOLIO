"""
84: Automated Trading Bot
Execute paper trades based on moving averages.
"""
def evaluate_ma_strategy(prices):
    short_ma = sum(prices[-3:]) / 3
    long_ma = sum(prices[-5:]) / 5
    if short_ma > long_ma:
        return "BUY"
    return "SELL/HOLD"

if __name__ == "__main__":
    p = [10, 11, 12, 13, 15, 16]
    print("Strategy Signal:", evaluate_ma_strategy(p))
