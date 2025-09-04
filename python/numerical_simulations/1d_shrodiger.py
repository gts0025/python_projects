import numpy as np
import matplotlib.pyplot as plt 
plank = 10
i = 2.0j
b = 5
c = 10
dt = 0.01
size = 20
dx = 1
cells = round(2*size/dx)

potential = np.zeros([cells])
line = np.linspace(-size/2,size/2,cells)
wave = np.zeros(shape=[cells],dtype=complex)
wave.imag = 1/(np.exp(line**2))
potential = (abs(line) > 5)*1




        
def show(steps,substeps):
    for step in range(steps):
        plt.title(f"shrodiger equation: step:{step*substeps}")
        
        plt.plot(line,potential,label = "potential")
        plt.plot(line,wave.real,label = "real wave")
        #plt.plot(line,wave.imag,label = "imag wave")
        
        plt.pause(0.001)
        plt.clf()

        for substep in range(substeps):
            d2ux = (wave[2:] + wave[:-2] - 2*wave[1:-1])/(dx**2)
            wave[1:-1] += ((d2ux*b + potential[1:-1]*wave[1:-1])/(i*plank))*dt
        

show(1000,10)
plt.show()