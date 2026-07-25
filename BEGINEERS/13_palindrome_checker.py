"""
13: Palindrome Checker
A script to reverse strings and check for symmetry.
"""
def is_palindrome(s):
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    test_str = "A man, a plan, a canal: Panama"
    print(f"Is '{test_str}' a palindrome?", is_palindrome(test_str))
