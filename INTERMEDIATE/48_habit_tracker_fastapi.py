"""
48: Habit Tracker API (FastAPI)
Build RESTful endpoints using FastAPI.
"""
try:
    from fastapi import FastAPI
    app = FastAPI()

    @app.get("/habits")
    def get_habits():
        return [{"habit": "Read 20 mins", "status": "Done"}]
except ImportError:
    print("FastAPI not installed. Run: pip install fastapi uvicorn")
