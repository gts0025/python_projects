import numpy as np
import matplotlib.pyplot as plt 
plank = 0.1
i = 1j
m = 1
dt = 0.001
size  = 10
dx = 0.4
cells = round(size/dx)

line = np.linspace(-size/2,size/2,cells)
wave = np.zeros(shape=[cells],dtype=complex)
wave.imag = (1/np.exp(line*line))


fig = plt.figure()
ax = fig.add_subplot()


        
def show(steps,substeps):
    for step in range(steps):
        plt.title(f"shrodiger equation: time:{round(step*substeps*dt*plank)}s")
    
        ax.set_ylim(-1,1)
        ax.plot(line,wave.real)
        ax.plot(line,wave.imag)
        ax.plot(line,abs(wave)**2)
        plt.pause(0.001)
        ax.cla()

        for substep in range(substeps):
            d2ux = (wave[2:] + wave[:-2] - 2*wave[1:-1])/(dx**2)
            wave[1:-1] += ( ( -d2ux*(plank**2/(2*m)) ) / (plank*i) )*dt
            wave[0] = 0
            wave[-1] = 0
        

show(2000,80)
plt.show()