import numpy as np
import matplotlib.pyplot as plt
grid = np.zeros([100,100,2])
charge = np.zeros_like(grid[:,:,0])
charge[20:30,45:55] = 10 
charge[70:80,45:55] = -10 

def solve(grid):
    div_x = grid[2:,1:-1,0]-grid[:-2,1:-1,0]
    div_y = grid[1:-1,2:,1]-grid[1:-1,:-2,1]
    div = (div_x + div_y)*0.98
    div -= charge[1:-1,1:-1]

    grid[2:,1:-1,0] -= div/4
    grid[:-2,1:-1,0] += div/4
    grid[1:-1,2:,1] -= div/4
    grid[1:-1,:-2,1] += div/4

    




def divergence(grid):
    div_x = grid[2:,1:-1,0]-grid[:-2,1:-1,0]
    div_y = grid[1:-1,2:,1]-grid[1:-1,:-2,1]
    div = div_x + div_y

    # pad back to full size (so we can display it as 400x400)
    full_div = np.zeros_like(grid[:,:,0])
    full_div[1:-1,1:-1] = div
    return full_div

running = True

plt.set_cmap("jet")
Y, X = np.mgrid[0:grid.shape[0], 0:grid.shape[1]]
plt.title("∇⋅U = Q")
for i in range(100):
    plt.title("∇⋅U = Q")
    plt.imshow(divergence(grid),vmin = charge.min(), vmax = charge.max())
    plt.colorbar()
    plt.streamplot(X, Y, grid[:,:,1], grid[:,:,0], density=1, color="k")
    for i in range(1):
        solve(grid)
    plt.pause(0.001)
    plt.clf()