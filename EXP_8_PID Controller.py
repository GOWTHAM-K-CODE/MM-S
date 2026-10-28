import numpy as np
import matplotlib.pyplot as plt

mass, g, dt = 1.5, 9.81, 0.1
t = np.arange(0, 10 + dt, dt)

z_setpoint = 10
Kp, Ki, Kd = 2.0, 0.1, 0.5

error_sum = 0
z, v = 0, 0
prev_error = z_setpoint - z
z_history = []

for i in range(len(t)):
    error = z_setpoint - z
    error_sum += error * dt
    d_error = (error - prev_error) / dt

    thrust = mass * g + Kp * error + Ki * error_sum + Kd * d_error
    a = (thrust - mass * g) / mass

    v += a * dt
    z += v * dt

    prev_error = error
    z_history.append(z)

plt.plot(t, z_history, label="Drone Altitude")
plt.axhline(10, color='r', linestyle='--', label="Target (10 m)")
plt.title("Altitude Hold with PID Control")
plt.xlabel("Time (s)")
plt.ylabel("Altitude (m)")
plt.legend()
plt.grid()
plt.show()