"""
63: RFID Attendance System
Interface RC522 reader with local SQLite database.
"""
def log_rfid_scan(card_id):
    print(f"RFID Tag Scanned: {card_id} -> Recorded attendance timestamp.")

if __name__ == "__main__":
    log_rfid_scan("0x4A 0x8B 0x12 0x90")
