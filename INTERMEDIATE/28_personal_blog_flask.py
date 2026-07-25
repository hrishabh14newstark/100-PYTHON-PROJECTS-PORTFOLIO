"""
28: Personal Blog (Flask)
Build a basic routing app using Flask.
"""
try:
    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def home():
        return "Welcome to My Personal Python Blog!"

    if __name__ == "__main__":
        print("Starting Flask server...")
except ImportError:
    print("Flask not installed. Run: pip install flask")
