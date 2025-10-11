
# this file uses 1d wave equation to 


import os
import numpy as np
import matplotlib.pyplot as plt


os.chdir(os.path.dirname(os.path.abspath(__file__)))

#initial gaussioan disturbance
x = np.linspace(-10,10,1000)
space = np.exp(-(x*x))

up = space
uc = space

c = 1# density
d = 0# viscosity
dx = x[1]-x[0]


"""
 
c*dt/dx < 1

c*dt < dx
dt < dx/c

"""

dt = (dx/c)


data = [] # final sound data 


"""
  (-up - 2*uc + un)/dt^2 = d2ux
  (-up - 2*uc)/dt^2 - d2ux  =  -un/dt^2 
  2uc - up - d2ux*dt^2 =  - un
  -(2uc - up - d2ux*dt^2) = un

    -(2uc - up - d2ux*dt^2) = un



"""

#integration function

#@njit(fastmath=True)

def second(data):
    d2ux = np.zeros_like(data)
    d2ux[1:-1] = (data[2:] + data[:-2] - 2*data[1:-1])/dx**2
    return d2ux

def wave_step(uc, up, c, dt):
    d2ux = second(uc)

    un  = (2*uc - up +  (c**2)*(d2ux)*(dt**2)  - ((uc-up)/dt)*d) 
    up = uc
    uc = un

    un *= 1-(d*dt)
    uc[0] = uc[1]*0
    uc[-1] = uc[-2]*0

    return uc,up

def energy(uc, up, c,dt):
    ut = (uc-up)/dt
    ux = np.gradient(ut)
    energy = ((ux**2 + ut**2)/(2*c)).sum()
    return energy


#plotting simulation itself

fig,ax = plt.subplots(2,1)

def viz_sumualtion(iterations,uc, up, c, dt):
    
    for i in range(iterations):
    
        plt.cla()
        plt.title(f"1d wave equation. step:{i}")
        
        for j in range(10):
            uc,up = wave_step(uc, up, c, dt)

        et.append(energy(uc, up, c, dt))
        if i > 0:
            et[-1] = (et[-1]+et[-2])/2 

        
        ax[0].clear()
        ax[1].clear()

        ax[0].plot(x,uc)
        ax[0].set_ylim(-1,1)

        ax[1].plot(et)
        

        #plt.ylim(-1,1)
        plt.pause(0.01)
        

et = []
viz_sumualtion(1000,uc, up, c, dt)
