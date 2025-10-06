import os
import seaborn as sns
import matplotlib.pyplot as plt
import fourier
import sounddevice as sdvc

os.chdir(os.path.dirname(os.path.abspath(__file__)))

import numpy as np 
from scipy.io import wavfile

rate = 10000
duration = 1
time = np.linspace(0,duration,int(rate*duration))
dt = 1/rate

curr_x = 400
last_x = 400

k = -((np.pi*2)*10)**2
f = np.sqrt(abs(k))/(2*np.pi)
data = []

for i in range(int(rate*duration)):

    # d2ut = lu - 2cu + nu
    # d2ut = kx
    # (lu - 2cu + nu)/dt^2 = kx
    # nu/dt^2 = (lu - 2cu)/dt^2 + kx
    # nu = -(lu - 2cu) + kx*dt^2

    next = -(last_x - 2*curr_x) + k*curr_x*dt**2     
    data.append(curr_x)

    last_x = curr_x
    curr_x = next

    progress = i/(rate*duration)
    if i % 5000 == 0:
        progress = i / (rate*duration) * 100  # in percent
        print(f"Progress: {progress:.2f}%")



sim_data = np.array(data,np.int16)

frequency = fourier.forward(sim_data,time,[f/2,f + f/2],400)
frequency = np.array(frequency)
sdvc.play(sim_data)

plt.title("fourier series on the numerical hooke's law ")
sns.lineplot(x = frequency[:,0],y = np.sqrt(frequency[:,1]**2 + frequency[:,2]**2))
plt.xlabel("frequencies")
plt.ylabel("amplitudes")
plt.show()


wavfile.write("hook_law_sim.wav",rate,sim_data)


