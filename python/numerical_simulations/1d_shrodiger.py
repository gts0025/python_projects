import numpy as np
import matplotlib.pyplot as plt 
import os
plt.style.use("dark_background")
os.chdir(os.path.dirname(os.path.abspath(__file__)))

plank = 0.1
i = 1j
m = 2
dt = 0.01
size  = 20
dx = 0.5
cells = round(size/dx)

line = np.linspace(-size/2,size/2,cells)
wave = np.zeros(shape=[cells],dtype=complex)
wave.imag = (1/np.exp(line*line))


fig = plt.figure()
ax = fig.add_subplot()


frames = []
def show(steps,substeps):
    for step in range(steps):
        plt.title(f"shrodiger equation: time:{round(step*substeps*dt*plank)}s")
    
        ax.set_ylim(-1,1)
        ax.plot(line,abs(wave)**2, linewidth = 2, label = "probability")
        ax.plot(line,wave.real,linewidth = 1, linestyle = "--",  label = "real")
        ax.plot(line,wave.imag,linewidth = 1, linestyle = "--", label = "imaginary")
        
        ax.legend()
        
        plt.pause(0.001)
        plt.savefig("1d_shrodinger.png")
        ax.cla()

        for substep in range(substeps):
            d2ux = (wave[2:] + wave[:-2] - 2*wave[1:-1])/(dx**2)
            wave[1:-1] += ( ( -d2ux*(plank**2/(2*m)) ) / (plank*i) )*dt
            wave[0] = 0
            wave[-1] = 0
        

show(500,80)
plt.show()