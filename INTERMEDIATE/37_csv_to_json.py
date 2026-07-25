"""
37: CSV to JSON Converter
A data formatting script for data ingestion.
"""
import csv
import json

def csv_to_json(csv_file, json_file):
    data = []
    try:
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        with open(json_file, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Converted {csv_file} to {json_file}")
    except FileNotFoundError:
        print("CSV file not found.")

if __name__ == "__main__":
    print("CSV to JSON converter ready.")
