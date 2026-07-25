"""
90: Data Pipeline (ETL)
Scrape, clean, and warehouse data.
"""
def run_etl():
    # Extract
    raw_data = ["  data_1 ", "data_2  ", "DATA_3"]
    # Transform
    cleaned = [d.strip().lower() for d in raw_data]
    # Load
    print("Loaded Clean Data into Warehouse:", cleaned)

if __name__ == "__main__":
    run_etl()
