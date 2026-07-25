"""
56: IoT Battery Capacity Estimator
Calculate total mAh over time from raw current logs.
"""
def calculate_mah(current_samples_ma, interval_sec):
    total_mas = sum(current_samples_ma) * interval_sec
    return total_mas / 3600.0

if __name__ == "__main__":
    samples = [120, 118, 122, 119, 121] # mA
    capacity = calculate_mah(samples, interval_sec=1)
    print(f"Estimated consumption: {capacity:.4f} mAh")
