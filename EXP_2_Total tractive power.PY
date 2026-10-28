import pandas as pd 
 
mass = 1200      # kg 
g = 9.81         # m/s^2 
Cr = 0.015 
dt = 1           # s 
Cd = 0.28 
A = 2.2          # m^2 
rho = 1.225      # kg/m^3 
 
df = pd.DataFrame({'time': list(range(5)), 
                   'speed': list(range(0, 21, 5))})   # m/s 
 
F_roll = mass * g * Cr 
df['acceleration'] = df['speed'].diff() / dt 
df = df.fillna({'acceleration': 0}) 
 
df['F_aero'] = 0.5 * rho * Cd * A * df['speed'] ** 2 
df['F_inertia'] = mass * df['acceleration'] 
df['F_total'] = F_roll + df['F_aero'] + df['F_inertia'] 
df['power'] = df['F_total'] * df['speed'] 
 
print(df[['time', 'speed', 'acceleration', 'F_total', 'power']])