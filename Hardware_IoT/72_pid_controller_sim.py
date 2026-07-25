"""
72: PID Controller Simulation
Visualize tuning parameters (P, I, D) for a heating element.
"""
class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.prev_error = 0
        self.integral = 0

    def compute(self, setpoint, pv):
        error = setpoint - pv
        self.integral += error
        derivative = error - self.prev_error
        self.prev_error = error
        return (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative)

if __name__ == "__main__":
    pid = PIDController(2.0, 0.1, 0.05)
    out = pid.compute(setpoint=100, pv=75)
    print("PID Output Signal:", out)
