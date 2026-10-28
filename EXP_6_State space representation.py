import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import StateSpace, lsim

A = np.array([[0, 1], [0, 0]])
B = np.array([[0], [1]])
C = np.eye(2)
D = np.zeros((2, 1))

sys = StateSpace(A, B, C, D)
t = np.linspace(0, 5, 6)
u = 0.5 * np.ones_like(t)

_, y, _ = lsim(sys, U=u, T=t)

print("Time(s)  Pitch Angle(rad)  Pitch Rate(rad/s)")
for i in range(len(t)):
    print(f"{t[i]:6.1f}  {y[i,0]:16.2f}  {y[i,1]:17.2f}")

plt.plot(t, y[:, 0], 'o-', label="Pitch Angle (rad)")
plt.plot(t, y[:, 1], 's-', label="Pitch Rate (rad/s)")
plt.xlabel("Time (s)")
plt.ylabel("Response")
plt.title("Drone Pitch Dynamics")
plt.legend()
plt.grid(True)
plt.show()