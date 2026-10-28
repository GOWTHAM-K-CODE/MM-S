import numpy as np
import matplotlib.pyplot as plt

target = np.array([5.0, 5.0])
pos = np.array([0.0, 0.0])
vel = np.array([0.0, 0.0])

dt = 0.1
Kp = 1.0
positions = []

for t in range(100):
    error = target - pos
    acc = Kp * error
    vel += acc * dt
    pos += vel * dt
    positions.append(pos.copy())

positions = np.array(positions)

print("Final Position:", np.round(pos, 2))
print("Target Position:", target)

plt.plot(positions[:, 0], positions[:, 1], label="Trajectory")
plt.plot(0, 0, 'go', label="Start")
plt.plot(5, 5, 'ro', label="Target")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.legend()
plt.grid(True)
plt.title("2D Drone Waypoint Tracking")
plt.axis("equal")
plt.show()
