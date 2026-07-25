"""
08: Unit Converter
A dictionary-based tool to convert lengths, weights, or temperatures.
"""
CONVERSIONS = {
    "km_to_miles": 0.621371,
    "miles_to_km": 1.60934,
    "kg_to_lbs": 2.20462,
    "lbs_to_kg": 0.453592
}

def convert(val, conversion_type):
    return val * CONVERSIONS.get(conversion_type, 1.0)

if __name__ == "__main__":
    print("10 km in miles:", convert(10, "km_to_miles"))
