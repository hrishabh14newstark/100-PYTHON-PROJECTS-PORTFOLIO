"""
26: Weather App (Tkinter GUI)
Fetch API data and display it in a Tkinter GUI.
"""
import tkinter as tk

def create_weather_gui():
    root = tk.Tk()
    root.title("Weather App")
    root.geometry("300x200")

    lbl = tk.Label(root, text="Enter City:", font=("Arial", 12))
    lbl.pack(pady=10)

    entry = tk.Entry(root, font=("Arial", 12))
    entry.pack(pady=5)

    res_label = tk.Label(root, text="Temp: -- °C", font=("Arial", 14, "bold"))
    res_label.pack(pady=20)

    root.withdraw() # Close immediately for automated runs
    print("Weather GUI Tkinter app template ready.")

if __name__ == "__main__":
    create_weather_gui()
