"""
58: Relay Switch Controller
Home automation logic using Raspberry Pi GPIO pins.
"""
def toggle_relay(pin, state):
    print(f"[GPIO] Setting Relay Pin {pin} to state: {state}")

if __name__ == "__main__":
    toggle_relay(18, "HIGH")
