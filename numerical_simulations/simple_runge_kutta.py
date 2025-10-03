# runge kutta  aproximation:


import matplotlib.pyplot as plt
import numpy as np

x_past = 10
x_current = 10

x = 10.1
s = 0


m = 1
k = 1
dt = 0.1

leap_list = []
euler_list = []
def leapfrog_run():

    
    global x_past
    global x_current 
    global m 
    global k
    global dt

    # d2ut = k*x:
    # (xp + xf - 2*xc)/dt^2 = -k*xc
    # xf/dt^2 =  -(xp - 2xc)/dt^2 -k*xc:
    # xf =  -xp + 2xc -k*xc/dt: 
    #  
    x_future = -x_past + 2*x_current - k*x_current*dt**2
    x_past = x_current
    x_current = x_future
    leap_list.append(x_current)



def euler_run():

    
    global x
    global s 
    global m 
    global k
    global dt

    # d2ut = k*x:
    # (xp + xf - 2*xc)/dt^2 = -k*xc
    # xf/dt^2 =  -(xp - 2xc)/dt^2 -k*xc:
    # xf =  -xp + 2xc -k*xc/dt: 
    #  
    f = -k*x
    s += f*dt
    x += s*dt
    
    euler_list.append(x)



for i in range(100):
    leapfrog_run()
    euler_run()
    plt.pause(0.01)
    plt.cla()

    plt.plot(euler_list)
    plt.plot(leap_list)
    
plt.show()
    
    