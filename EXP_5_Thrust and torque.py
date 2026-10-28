import numpy as np

m = 1.5
g = 9.81
L = 0.25
kf = 3e-6
km = 1e-7

omega = np.array([400, 420, 390, 410])

# Individual rotor thrusts
thrust = kf * omega**2

# Total thrust
Fz = np.sum(thrust)

# Torques
Tx = L * kf * (omega[1]**2 - omega[3]**2)
Ty = L * kf * (omega[2]**2 - omega[0]**2)
Tz = km * (omega[0]**2 - omega[1]**2
           + omega[2]**2 - omega[3]**2)

print("Individual Rotor Thrusts:")
for i, t in enumerate(thrust, 1):
    print(f"Rotor {i}: {t:.4f} N")

print(f"Total Thrust: {Fz:.4f} N")
print(f"Roll Torque: {Tx:.4f} Nm")
print(f"Pitch Torque: {Ty:.4f} Nm")
print(f"Yaw Torque: {Tz:.4f} Nm")