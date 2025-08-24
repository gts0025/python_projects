import numpy as np
import matplotlib.pyplot as plt  
import imageio

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


plt.style.use("dark_background")
plt.title("Allen-cahn model for reaction diffusion")

u = (np.random.random([200,200]) + -0.5)*2
D = 1
R = 0.7
dt = 0.01


frames = []
for i in range(600):

    #laplacian poerator
    d2u = (
        u[2:,1:-1] + u[:-2,1:-1] - 2*u[1:-1,1:-1] + 
        u[1:-1,2:] + u[1:-1,:-2] - 2*u[1:-1,1:-1] 
        )
    
    #difuse the material
    u[1:-1,1:-1] += d2u*D*dt

    #apply reaction 
    u += (u-u**3)*R*dt

    #boudary conditions:  du/dx( x = 0, x = L, y = 0; y = L) = 0
    u[0,1:-1] = u[1,1:-1]
    u[-1,1:-1] = u[-2,1:-1]

    u[1:-1,0] = u[1:-1,1]
    u[1:-1,-1] = u[1:-1,-2]


    #plot the data:
    plt.imshow(u,cmap="jet",vmax=1.5,vmin=-1.5)
    plt.title("Allen-cahn model for reaction diffusion")

    plt.colorbar()
    plt.savefig("frame.png")
    frames.append(imageio.imread("frame.png"))
    os.remove("frame.png")
    #update and clear screen
    plt.pause(0.01)
    plt.clf()


imageio.mimsave("allen_cahn.gif", frames, fps=20)
from gif_to_mp4 import Converter
final = Converter("allen_cahn.gif","allen_cahn.mp4")

