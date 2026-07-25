"""
97: Custom Language Compiler
Build tokenizer, parser, and interpreter from scratch.
"""
class Tokenizer:
    def __init__(self, code):
        self.code = code
    def tokenize(self):
        return self.code.replace(";", "").split()

if __name__ == "__main__":
    t = Tokenizer("VAR x = 10;")
    print("Tokens:", t.tokenize())
