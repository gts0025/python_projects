
# this file uses 1d wave equation to 


import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import fourier
import sounddevice as sdvc

os.chdir(os.path.dirname(os.path.abspath(__file__)))

sps,voice = wavfile.read("my_voice_record.wav")
print(f"samples per second: {sps}")
voice = voice.astype(np.float32)  # cast to float
if voice.ndim > 1:
    voice = voice[:,0]

voice /= np.max(np.abs(voice)) 


#sps = 44000 #steps per second
ftime = int(voice.shape[0]/sps)# stopping time


#initial gaussioan disturbance
x = np.linspace(0,10,300)
space = np.zeros_like(x)
up = space
uc = space

k = 300# density
d = 4e-8 # viscosity
dt = 1/sps # stime step size
data = [] # final sound data 


"""
  (-up - 2*uc + un)/dt^2 = d2ux
  (-up - 2*uc)/dt^2 - d2ux  =  -un/dt^2 
  2uc - up - d2ux*dt^2 =  - un
  -(2uc - up - d2ux*dt^2) = un

    -(2uc - up - d2ux*dt^2) = un



"""

#integration function
def wave_step():
    global uc, up, k, dt
    d2ux = np.zeros_like(up)
    dx = x[1]-x[0]
    #dx = 1

    d2ux[1:-1] = k**2*(uc[2:] + uc[:-2] - 2*uc[1:-1])/dx**2
    un  = (2*uc - up + (d2ux*dt*dt)  - ((uc-up)/dt)*d) 
    up = uc
    uc = un

    un *= 1-(d*dt)
    uc[0] = uc[1]
    uc[-1] = uc[-2]

#plotting simulation itself

def get_sound():
    global data
    
    for i in range(voice.shape[0]):
        wave_step()
        uc[100] = voice[i]
       
        data.append(uc[1])
    data = np.array(data)
    data /= np.max(np.abs(data)) 
    sound = np.int16(data*2e4)
    wavfile.write("1d wave_sound.wav",sps,sound)
    #final = wavfile.read("1d wave_sound.wav")
    #sdvc.play(voice,sps)
    #sdvc.wait()
    sdvc.play(sound,sps)
    sdvc.wait()
    #echo = voice + sound*0.1
    #sdvc.play(echo,sps)



def viz_sumualtion(iterations):
    
    for i in range(iterations):
    
        plt.cla()
        plt.title(f"1d wave equation. step:{i}")
        
        for j in range(30):
            uc[-2] = voice[i + sps]
            up[-2] = voice[i + sps]
        
            wave_step()
            
        plt.plot(uc)
        plt.ylim(-1,1)
        plt.pause(1/sps)

def viz_data():
    get_sound()
    plt.plot(data)
    



def viz_freq():
    get_sound()
    frequency = fourier.forward(data,np.linspace(0,ftime,ftime*sps),[0,1000],10000)
    frequency = np.array(frequency)

    
    plt.title("fourier series")
    plt.plot(frequency[:,0],np.sqrt(frequency[:,1]**2 + frequency[:,2]**2))
    plt.xlabel("frequencies")
    plt.ylabel("amplitudes")
    plt.show()


#viz_sumualtion(1000)
get_sound()
#viz_freq()


#plt.plot(data)
#plt.plot(voice)



#plt.show()

