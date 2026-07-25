"""
74: Capacitance Meter Script
Calculate RC time constants from raw DAQ inputs.
"""
import math

def calculate_capacitance(r_ohms, t_seconds):
    # V(t) = V0 * (1 - e^(-t/RC)) -> At t = RC, V = 63.2%
    c_farads = t_seconds / r_ohms
    return c_farads * 1e6 # uF

if __name__ == "__main__":
    uF = calculate_capacitance(r_ohms=10000, t_seconds=0.001)
    print(f"Measured Capacitance: {uF:.2f} uF")
