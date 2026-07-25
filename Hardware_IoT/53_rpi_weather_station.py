"""
53: Raspberry Pi Weather Station
Interface with physical I2C/SPI sensors (e.g., BME280).
"""
def read_bme280():
    # Simulated sensor readings
    return {"temp_c": 24.5, "humidity": 55.2, "pressure_hpa": 1013.25}

if __name__ == "__main__":
    print("Sensor Data:", read_bme280())
