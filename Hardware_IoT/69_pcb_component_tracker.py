"""
69: PCB Component Tracker
Database app for managing electronics lab inventory.
"""
inventory = {}

def add_part(part_no, desc, qty):
    inventory[part_no] = {"desc": desc, "qty": qty}
    print(f"Added part: {part_no} (Qty: {qty})")

if __name__ == "__main__":
    add_part("STM32F401RBT6", "MCU ARM Cortex-M4", 25)
