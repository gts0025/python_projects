import os
import seaborn as sns
import matplotlib.pyplot as plt
import fourier

os.chdir(os.path.dirname(os.path.abspath(__file__)))

import numpy as np 
from scipy.io import wavfile

rate = 10000
duration = 3
time = np.linspace(0,duration,rate*duration)
dt = 1/rate
x = 400
s = 0
u = 10
k = -((np.pi*2*800)**2)
data = []

for i in range(rate*duration):
    s += k*x*dt
    x += s*dt
    s -= s*u*dt
    data.append(x)
    progress = i/(rate*duration)
    if i % 5000 == 0:
        progress = i / (rate*duration) * 100  # in percent
        print(f"Progress: {progress:.2f}%")



sim_data = np.array(data,np.int16)
wavfile.write("hook_law_sim.wav",rate,sim_data)

#sns.lineplot(x = time,y = sim_data)
frequency = fourier.forward(sim_data,time,[0,2*np.sqrt(abs(k))/(np.pi*2)],2000)
frequency = np.array(frequency)
sns.lineplot(x = frequency[:,0],y = np.sqrt(frequency[:,1]**2 + frequency[:,2]**2))
plt.show()


