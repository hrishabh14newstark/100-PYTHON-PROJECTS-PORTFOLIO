"""
68: CAN Bus Sniffer
Read and decode automotive or industrial network frames using python-can.
"""
def sniff_can_bus(channel="can0"):
    try:
        import can
        print(f"Listening to CAN interface {channel}...")
    except ImportError:
        print("python-can package required.")

if __name__ == "__main__":
    sniff_can_bus()
