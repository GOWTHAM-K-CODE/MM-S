1. Calculate Rolling Resistance Energy Consumption
   Expt. No.: 01
   import pandas as pd
   import numpy as np

mass = 1200
Cr = 0.015
g = 9.81

time = [0, 1, 2, 3, 4]
speed = [0, 5, 10, 15, 20]

df = pd.DataFrame({'time': time, 'speed': speed})

df['F_roll'] = mass * g * Cr
df['power'] = df['F_roll'] * df['speed']

energy = np.trapezoid(df['power'], df['time'])

print(df)
print(f"Rolling Force = {massgCr:.2f} N")
print(f"Total Energy = {energy:.2f} J")

2. Simulate Total Tractive Power Demand
   Expt. No.: 02

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mass = 1200
Cr = 0.015
Cd = 0.28
A = 2.2
rho = 1.225
g = 9.81

time = [0, 1, 2, 3, 4]
speed = [0, 5, 10, 15, 20]

df = pd.DataFrame({'time': time, 'speed': speed})

df['acceleration'] = np.gradient(speed, 1)
df['F_roll'] = mass * g * Cr
df['F_aero'] = 0.5 * rho * Cd * A * df['speed']**2
df['F_inertia'] = mass * df['acceleration']
df['F_total'] = df['F_roll'] + df['F_aero'] + df['F_inertia']
df['power'] = df['F_total'] * df['speed']

print(df.round(2))

plt.plot(time, df['power'], marker='o')
plt.xlabel('Time (s)')
plt.ylabel('Power (W)')
plt.title('Tractive Power vs Time')
plt.grid()
plt.show()

3. Estimate Battery Energy Required for a Trip
   Expt. No.: 03

import pandas as pd
import numpy as np

mass = 1200
Cr = 0.015
g = 9.81
efficiency = 0.9

time = [0, 1, 2, 3, 4]
speed = [0, 5, 10, 15, 20]

df = pd.DataFrame({'time': time, 'speed': speed})

df['acceleration'] = np.gradient(speed, 1)
df['F_roll'] = mass * g * Cr
df['F_inertia'] = mass * df['acceleration']
df['F_total'] = df['F_roll'] + df['F_inertia']
df['power'] = df['F_total'] * df['speed']

energy_J = np.trapezoid(df['power'], time)
energy_Wh = energy_J / 3600
battery_Wh = energy_Wh / efficiency

print(df.round(2))
print(f"Energy = {energy_J:.2f} J")
print(f"Energy = {energy_Wh:.2f} Wh")
print(f"Battery Energy = {battery_Wh:.2f} Wh")

4. 

import pandas as pd
import numpy as np

mass = 1200
regen_eff = 0.7

time = [0, 1, 2, 3, 4, 5, 6, 7]
speed = [0, 5, 10, 15, 20, 15, 13, 11]

df = pd.DataFrame({'time': time, 'speed': speed})

df['acceleration'] = df['speed'].diff().fillna(0)
df['regen_power'] = np.where(
df['acceleration'] < 0,
-mass * df['acceleration'] * df['speed'],
0
)

df['energy_Wh'] = df['regen_power'] * regen_eff / 3600
total_energy = np.trapezoid(df['energy_Wh'], time)

print(df.round(2))
print(f"Energy Recovered = {total_energy:.2f} Wh")

5. Modeling Drone Thrust and Torque
   Expt. No.: 05

import numpy as np

mass = 1.5
L = 0.25
kf = 3e-6
km = 1e-7

omega = np.array([400, 420, 390, 410])

thrust = kf * omega**2
Fz = np.sum(thrust)

Tx = L * kf * (omega[1]**2 - omega[3]**2)
Ty = L * kf * (omega[2]**2 - omega[0]**2)
Tz = km * (omega[0]**2 - omega[1]**2
+ omega[2]**2 - omega[3]**2)

print("Individual Thrusts:", thrust)
print(f"Total Thrust = {Fz:.4f} N")
print(f"Weight = {mass*9.81:.4f} N")
print(f"Roll Torque = {Tx:.6f} Nm")
print(f"Pitch Torque = {Ty:.6f} Nm")
print(f"Yaw Torque = {Tz:.6f} Nm")
6. Implementing and Simulating State-Space Representation
Expt. No.: 06

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import StateSpace, lsim

A = np.array([[0., 1.],
[0., 0.]])
B = np.array([[0.],
[1.]])
C = np.eye(2)
D = np.zeros((2, 1))

sys = StateSpace(A, B, C, D)

t = np.linspace(0, 5, 501)
u = 0.5 * np.ones_like(t)

_, y, _ = lsim(sys, U=u, T=t)

plt.plot(t, y[:, 0], label='Pitch Angle')
plt.plot(t, y[:, 1], label='Pitch Rate')
plt.xlabel('Time (s)')
plt.ylabel('State')
plt.title('Drone Pitch Dynamics')
plt.legend()
plt.grid()
plt.show()

7. Simulate 2D Drone Waypoint Navigation
   Expt. No.: 07

import numpy as np
import matplotlib.pyplot as plt

target = np.array([5.0, 5.0])
pos = np.array([0.0, 0.0])

Kp = 1.0
dt = 0.1

positions = [pos.copy()]

for i in range(100):
error = target - pos
pos = pos + Kp * error * dt
positions.append(pos.copy())

positions = np.array(positions)

print("Final Position:", pos)

plt.plot(positions[:, 0], positions[:, 1],
label='Drone Path')
plt.plot(5, 5, 'ro', label='Target')
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.title('2D Drone Navigation')
plt.legend()
plt.grid()
plt.show()
8. Simulate Altitude Hold Using PID Controller
Expt. No.: 08

import numpy as np
import matplotlib.pyplot as plt

mass = 1.5
g = 9.81
dt = 0.1

t = np.arange(0, 10 + dt, dt)

setpoint = 10
Kp = 2.0
Ki = 0.1
Kd = 0.5

z = 0.0
v = 0.0
error_sum = 0.0
prev_error = setpoint - z
z_history = []

for _ in t:
error = setpoint - z
error_sum += error * dt
d_error = (error - prev_error) / dt

thrust = mass*g + Kp*error + Ki*error_sum + Kd*d_error  
acceleration = (thrust - mass*g) / mass  

v += acceleration * dt  
z += v * dt  

prev_error = error  
z_history.append(z)

print(f"Final Altitude = {z_history[-1]:.2f} m")
print(f"Peak Altitude = {max(z_history):.2f} m")

plt.plot(t, z_history, label='Altitude')
plt.axhline(setpoint, linestyle='--', label='Target')
plt.xlabel('Time (s)')
plt.ylabel('Altitude (m)')
plt.title('PID Altitude Hold')
plt.legend()
plt.grid()
plt.show()
