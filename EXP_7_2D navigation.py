import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Target position
target = np.array([5.0, 5.0])
pos = np.array([0.0, 0.0])
vel = np.array([0.0, 0.0])

dt = 0.1
Kp = 1.0
positions = []
times = []

# Drone waypoint tracking
for t in range(100):
    error = target - pos
    acc = Kp * error
    vel += acc * dt
    pos += vel * dt

    positions.append(pos.copy())
    times.append((t + 1) * dt)

positions = np.array(positions)

# Display table at 1-second intervals
sample_indices = [0, 9, 19, 29, 39, 49]

df = pd.DataFrame({
    "Time (s)": [0.0] + [1.0, 2.0, 3.0, 4.0, 5.0],
    "X (m)": [0.00] + [round(positions[i, 0], 2)
                        for i in sample_indices[:5]],
    "Y (m)": [0.00] + [round(positions[i, 1], 2)
                        for i in sample_indices[:5]]
})

print(df.to_string(index=False))

print("\nFinal Position:", np.round(pos, 2))
print("Target Position:", target)

# Plot trajectory
plt.figure(figsize=(8, 6))
plt.plot(positions[:, 0], positions[:, 1],
         label="Trajectory")
plt.plot(0, 0, 'go', label="Start")
plt.plot(target[0], target[1], 'ro', label="Target")

plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.title("2D Drone Waypoint Tracking")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.show()