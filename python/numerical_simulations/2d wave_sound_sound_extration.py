import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import fourier

os.chdir(os.path.dirname(os.path.abspath(__file__)))


sps = 10000 #steps per second
ftime = 5 # stopping time


#initial gaussioan disturbance
x = np.linspace(-10,10,90)
gaussian = np.exp(-(x**2))

up = gaussian
uc = gaussian

k = 2*np.pi*1600**2 # density
d = -0.000001
dt = 1/sps # stime step size
data = [] # final sound data 


"""
  (-up - 2*uc + un)/dt^2 = d2ux
  (-up - 2*uc)/dt^2 - d2ux  =  -un/dt^2 
  2uc - up - d2ux*dt^2 =  - un
  -(2uc - up - d2ux*dt^2) = un


"""

#integration function
def wave_step():
    global uc, up, k, dt
    d2ux = np.zeros_like(up)
    d2ux[1:-1] = k*(uc[2:] + uc[:-2] - 2*uc[1:-1])
    un  = (2*uc - up + (d2ux*dt*dt) + d*d2ux*dt) 
    up = uc
    uc = un

    up[0],up[-1], un[0], un[-1] = (0,0,0,0)

#plotting simulation itself

def get_sound():
    global data
    for i in range(ftime*sps):
        wave_step()
        data.append(uc[1])
    data = np.array(data)*600
    sound = np.int16(np.array(data))
    wavfile.write("1d wave_sound.wav",sps,sound)


def viz_sumualtion(iterations):
    
    for i in range(iterations):
    
        plt.cla()
        plt.title(f"1d wave equation. step:{i}")
        
        for i in range(30):
            wave_step()
        plt.plot(uc)
        plt.ylim(-1,1)
        plt.pause(0.001)

def viz_data():
    get_sound()
    plt.plot(data)

def viz_freq():
    get_sound()
    frequency = fourier.forward(data,np.linspace(0,ftime,ftime*sps),[000,1000],10000)
    frequency = np.array(frequency)


    plt.title("fourier series")
    plt.plot(frequency[:,0],np.sqrt(frequency[:,1]**2 + frequency[:,2]**2))
    plt.xlabel("frequencies")
    plt.ylabel("amplitudes")
    plt.show()



#get_sound()
viz_freq()
viz_sumualtion(1000)


plt.show()

