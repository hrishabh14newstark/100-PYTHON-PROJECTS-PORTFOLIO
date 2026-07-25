"""
81: Credit Card Fraud Detection
Anomaly detection using Pandas and machine learning models.
"""
def detect_fraud(transaction):
    # Isolation forest / threshold logic simulation
    return transaction.get("amount", 0) > 5000

if __name__ == "__main__":
    tx = {"id": 9912, "amount": 7500}
    print(f"Transaction {tx['id']} Fraud Alert:", detect_fraud(tx))
