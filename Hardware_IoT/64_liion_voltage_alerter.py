"""
64: Li-ion Voltage Alerter
Script that sends a webhook if cell voltage drops below 3.0V.
"""
def check_cell_voltage(v_cell):
    if v_cell < 3.0:
        print(f"[ALERT] Cell voltage critical: {v_cell}V! Sending alert webhook...")
    else:
        print(f"Cell voltage normal: {v_cell}V")

if __name__ == "__main__":
    check_cell_voltage(2.92)
