"""
22: Text-to-Speech Script
Convert strings to audio using pyttsx3.
"""
def speak(text):
    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except ImportError:
        print(f"[Text-To-Speech Fallback]: {text}")

if __name__ == "__main__":
    speak("Hello, welcome to Python project tutorials.")
