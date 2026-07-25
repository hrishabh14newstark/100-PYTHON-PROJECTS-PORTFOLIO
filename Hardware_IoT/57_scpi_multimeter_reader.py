"""
57: Automated Multimeter Reader
Parse SCPI commands from bench hardware.
"""
def send_scpi_cmd(cmd):
    print(f"Sending SCPI Command: {cmd}")
    return "+3.30012E+00"

if __name__ == "__main__":
    val = send_scpi_cmd("MEASure:VOLTage:DC?")
    print("DMM Reading:", val)
