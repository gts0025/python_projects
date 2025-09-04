import numpy as np
import matplotlib.pyplot as plt 
plank = 0.1
i = 1j
m = 1
dt = 0.01
size  = 20
dx = 0.2
cells = round(size/dx)

x_line = np.linspace(-size/2,size/2,cells)
y_line = np.linspace(-size/2,size/2,cells)
a_x,a_y = np.meshgrid(x_line,y_line)

wave = np.zeros(shape=[cells,cells],dtype=complex)
dist  = np.sqrt(a_x**2 + a_y**2)
gaussian = 1/np.exp(a_x**2 + a_y**2) 
wave.imag = (gaussian)


fig = plt.figure()
ax = fig.add_subplot()


        
def show(steps,substeps):
    for step in range(steps):
        plt.title(f"shrodiger equation: time:{round(step*substeps*dt*plank)}s")
    
        
        cont = ax.imshow(abs(wave)**2, cmap="jet")
        plt.pause(0.0001)
        ax.cla()

        for substep in range(substeps):
            d2ux = (wave[2:,1:-1] + wave[:-2,1:-1] - 2*wave[1:-1,1:-1])/(dx**2)
            d2uy = (wave[1:-1,2:] + wave[1:-1,:-2] - 2*wave[1:-1,1:-1])/(dx**2)
            wave[1:-1,1:-1] += ( ( -( d2ux+d2uy )*( plank**2/(2*m) ) ) / (plank*i) )*dt

        

show(2000,40)
plt.show()