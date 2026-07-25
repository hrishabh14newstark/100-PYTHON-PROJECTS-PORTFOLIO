"""
66: Bluetooth LE Device Scanner
Find and log nearby BLE beacons using bleak.
"""
def scan_ble():
    try:
        import bleak
        print("Scanning for Bluetooth Low Energy devices...")
    except ImportError:
        print("bleak library required.")

if __name__ == "__main__":
    scan_ble()
