"""
09: Basic Calculator
Implement functions for math operations.
"""
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error: Division by zero"

if __name__ == "__main__":
    print("10 + 5 =", add(10, 5))
    print("10 / 2 =", divide(10, 2))
