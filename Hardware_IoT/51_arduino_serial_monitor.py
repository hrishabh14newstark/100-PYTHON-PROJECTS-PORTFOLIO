"""
51: Arduino Serial Monitor
Read, log, and graph data from a microcontroller using pyserial.
"""
def read_serial(port="/dev/ttyUSB0", baud=9600):
    try:
        import serial
        print(f"Connecting to microcontroller on {port} at {baud} baud...")
    except ImportError:
        print("pyserial module not found. Run: pip install pyserial")

if __name__ == "__main__":
    read_serial()
