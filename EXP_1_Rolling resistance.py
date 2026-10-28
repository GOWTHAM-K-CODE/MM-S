import pandas as pd 
mass = 1200  
g = 9.81  
Cr = 0.015 
dt = 1  
data = {'time': [0, 1, 2, 3, 4], 'speed': [0, 5, 10, 15, 20]} 
df = pd.DataFrame(data) 
F_roll = mass * g * Cr 
df['energy_roll'] = F_roll * df['speed'] * dt
total_energy = df['energy_roll'].sum() 
print(df) 
print(f"Total Rolling Resistance Energy = {total_energy:.2f} J")