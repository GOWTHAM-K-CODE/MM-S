import pandas as pd 
import numpy as np 
 
data = {'time': [0, 1, 2, 3, 4, 5, 6, 7], 
        'speed': [0, 5, 10, 15, 20, 15, 13, 11]}   # m/s 
df = pd.DataFrame(data) 
 
mass = 1200      # kg 
dt = 1           # s 
regen_eff = 0.7  # 70 % efficient 
 
df['acceleration'] = df['speed'].diff() / dt 
df = df.fillna({'acceleration': 0}) 
 
df['regen_power'] = np.where(df['acceleration'] < 0, 
                             mass * df['acceleration'] * df['speed'], 0) 
df['energy_recovered_Wh'] = -df['regen_power'] * dt / 3600 * regen_eff 
total_recovered = df['energy_recovered_Wh'].sum() 
 
print(df[['time', 'speed', 'acceleration', 'regen_power', 'energy_recovered_Wh']]) 
print(f"Total Energy Recovered via Regenerative Braking: {total_recovered:.2f} Wh")