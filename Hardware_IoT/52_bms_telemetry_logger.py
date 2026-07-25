"""
52: Battery Charge/Discharge Logger
Parse telemetry data (voltage/temperature) from a BMS.
"""
import time

def log_bms_telemetry(voltage, current, temp):
    power = voltage * current
    print(f"[Telemetry] V: {voltage:.2f}V | I: {current:.2f}A | P: {power:.2f}W | Temp: {temp}°C")

if __name__ == "__main__":
    log_bms_telemetry(3.72, 1.5, 28.4)
