"""
71: Solar Efficiency Tracker
Correlate ambient lux sensor data with panel voltage output.
"""
def calculate_efficiency(lux, v_out, i_out, panel_area_m2=0.1):
    solar_irradiance_w_m2 = lux * 0.0079 # approx conversion
    power_in = solar_irradiance_w_m2 * panel_area_m2
    power_out = v_out * i_out
    return (power_out / power_in) * 100 if power_in > 0 else 0.0

if __name__ == "__main__":
    eff = calculate_efficiency(50000, 18.2, 0.45)
    print(f"Calculated Panel Efficiency: {eff:.2f}%")
