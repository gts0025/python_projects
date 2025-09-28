import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import fourier

os.chdir(os.path.dirname(os.path.abspath(__file__)))

sps,voice = wavfile.read("eleve_labs_sound_test.wav")

voice = voice.astype(np.float32)  # cast to float
voice /= np.max(np.abs(voice)) 


#sps = 44000 #steps per second
ftime = int(voice.shape[0]/sps)# stopping time

#no file testing:  
#sps = 1600
#ftime = 3

#initial gaussioan disturbance
x = np.linspace(-5,5,10)
gaussian = np.exp(-x**2)
#gaussian = np.zeros(20)
h = gaussian 
u = np.zeros_like(h)
s = 0 


k =  2*np.pi*10000 # density
d = 22
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

def derivative(field):
    zero = np.zeros_like(field)
    zero[1:-1] = field[2:]-field[:-2]
    return zero 

def second_derivative(field):
    zero = np.zeros_like(field)
    zero[1:-1] = field[2:]+field[:-2]- 2*field[1:-1]
    return zero 

def step(substeps):

    global u,h,k,dt,d
    #boundary cpndition
    h[0] = h[1]
    h[-1] = h[-2]
    u[0] = u[1]
    u[-1] = u[-2] 
    #pressure
    
    
    #solve
    dht = -(derivative(u*h) - second_derivative(h)*d)
    dut = -(derivative(h*k))
    u += dut*(dt/substeps)
    h += dht*(dt/substeps)

   

#plotting simulation itself

def get_sound():
    global data
    for i in range(ftime*sps):
        step(10)
        h[-1] = voice[i]
        h[-1] = voice[i]
       
        data.append(h[1]*1000)
    data = np.array(data)
    sound = np.int16(np.array(data))
    wavfile.write("1d gas_sound.wav",sps,sound)


def viz_sumualtion(iterations):
    
    for i in range(iterations):
    
        plt.cla()
        plt.title(f"1d wave equation. step:{i}")
        
       
        step(40)
        plt.plot(h)
        #plt.ylim(0,200)
        plt.pause(0.001)

def viz_data():
    get_sound()
   
    plt.plot(data,max_y = 1 )
    #plt.ylim(-1,2)

def viz_freq():
    get_sound()
    frequency = fourier.forward(data,np.linspace(0,ftime,ftime*sps),[0,1000],10000)
    frequency = np.array(frequency)


    plt.title("fourier series")
    plt.plot(frequency[:,0],np.sqrt(frequency[:,1]**2 + frequency[:,2]**2))
    plt.xlabel("frequencies")
    plt.ylabel("amplitudes")
    plt.show()



get_sound()
#viz_freq()
#plt.plot(data)
#plt.plot(voice)
viz_sumualtion(1000)


plt.show()

