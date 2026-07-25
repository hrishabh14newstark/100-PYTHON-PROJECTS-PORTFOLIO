"""
38: System Resource Monitor
Dashboard displaying CPU and RAM usage using psutil.
"""
def monitor_system():
    try:
        import psutil
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        print(f"CPU Usage: {cpu}% | RAM Usage: {ram}%")
    except ImportError:
        print("psutil not installed. Run: pip install psutil")

if __name__ == "__main__":
    monitor_system()
