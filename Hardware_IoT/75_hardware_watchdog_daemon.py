"""
75: Hardware Watchdog Daemon
Ping network devices and trigger relays to power-cycle them if they hang.
"""
import subprocess

def ping_device(ip):
    res = subprocess.run(["ping", "-c", "1", ip], stdout=subprocess.DEVNULL)
    return res.returncode == 0

if __name__ == "__main__":
    ip = "192.168.1.1"
    alive = ping_device(ip)
    print(f"Device {ip} status: {'ONLINE' if alive else 'OFFLINE'}")
