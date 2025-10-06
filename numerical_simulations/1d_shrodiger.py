import numpy as np
import matplotlib.pyplot as plt 
import os
import imageio

plt.style.use("dark_background")

plank = 0.1
i = 1j
m = 2
dt = 0.01
size  = 20
dx = 0.5
cells = round(size/dx)

line = np.linspace(-size/2,size/2,cells)
wave = np.zeros(shape=[cells],dtype=complex)
wave.imag = np.pi*(1/(line*line + 1))


fig = plt.figure()
ax = fig.add_subplot()


frames = []
def show(steps,substeps):
    for step in range(steps):

        if (step)%100 == 0:
            print(f"running: {round((step/steps)*100)}%")
        plt.title(f"shrodiger equation")
        ax.set_ylim(-1,1)
        ax.plot(line,abs(wave)**2, linewidth = 2, label = "probability")
        ax.plot(line,wave.real,linewidth = 1, linestyle = "--",  label = "real")
        ax.plot(line,wave.imag,linewidth = 1, linestyle = "--", label = "imaginary")
        ax.legend()
        plt.savefig("1d_shrodinger.png")
        ax.cla()
        frames.append(imageio.imread("1d_shrodinger.png"))
        
        for substep in range(substeps):
            d2ux = (wave[2:] + wave[:-2] - 2*wave[1:-1])/(dx**2)
            wave[1:-1] += ( ( -d2ux*(plank**2/(2*m)) ) / (plank*i) )*dt
            wave[0] = 0
            wave[-1] = 0

show(1500,40)

imageio.mimsave("1d_shrodinger.gif",frames,fps = 25)
os.remove("1d_shrodinger.png")
from gif_to_mp4 import Converter
final = Converter("1d_shrodinger.gif","1d_shrodinger.mp4")


