"""
14: Fibonacci Generator
Generate sequences using either recursion or iteration.
"""
def fibonacci(n):
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

if __name__ == "__main__":
    print("First 10 Fibonacci numbers:", fibonacci(10))
