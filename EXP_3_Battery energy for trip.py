import pandas as pd

mass, g, Cr, dt = 1200, 9.81, 0.015, 1
Cd, A, rho = 0.28, 2.2, 1.225
efficiency = 0.9

df = pd.DataFrame({
    'time': [0, 1, 2, 3, 4],
    'speed': [0, 5, 10, 15, 20]
})

df['acceleration'] = df['speed'].diff().fillna(0) / dt
F_total = (mass*g*Cr + 0.5*rho*Cd*A*df['speed']**2
           + mass*df['acceleration'])
df['power'] = F_total * df['speed']

df['distance'] = (df['speed'] + df['speed'].shift()) / 2 * dt
df['energy_Wh'] = ((df['power'] + df['power'].shift()) / 2 * dt / 3600).fillna(0)

energy = df['energy_Wh'].sum()
distance = df['distance'].sum()
battery = energy * 10000 / distance / efficiency

print(df[['time', 'power', 'energy_Wh']].round(2))
print(f"Battery Energy for 10 km = {battery/1000:.2f} kWh")