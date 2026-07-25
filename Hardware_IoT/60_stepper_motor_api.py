"""
60: Motor Control API
Send step and direction commands to a stepper motor driver.
"""
def step_motor(steps, direction, delay_us=500):
    print(f"Moving stepper motor {steps} steps in direction '{direction}'")

if __name__ == "__main__":
    step_motor(200, "CW")
