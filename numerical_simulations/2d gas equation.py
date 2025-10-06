#2d gas equation 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from PIL import Image
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

plt.style.use('dark_background')

#constants


img = Image.open("airfoil.png").convert('L')
im_data = np.array(img).astype(np.float32) / 255.0
bright = np.array(im_data)
bright[bright < 0.5] = 0
bright[bright >= 0.5] = 1
bright = np.zeros([100,100])
bd = 1# base density
max_speed = 1
bs = 2
mask = np.zeros_like(bright)


dt = 0.1
vd = 0.1
dd = 0.0
td = 0.01
id = 0.01

dx = 1
t_buoyancy = -0.01
substeps = 30
gravity = 0.0

#derivatves 

#restriction 

vr = (-max_speed,max_speed)
dr = (bd-3,bd+3) 

#fields


# Define the curve: centered horizontally

density = np.ones_like(bright)*bd
velocity_u = np.ones_like(bright)*0
velocity_v = np.ones_like(bright)*0
ink = np.zeros_like(bright)
heat = np.zeros_like(bright)*-2


figure,ax = plt.subplots(1,1,figsize=(5,5))
ax.set_aspect('equal')
#ax.axis("off")

implot =  plt.imshow(
    density, 
    cmap="inferno",
    vmin=-0,
    vmax=2
    )


def derivative(field, axis):
    zero_field = np.zeros_like(field)
    if axis == 0:
        zero_field[1:-1,1:-1]+=( 
            (field[2:, 1:-1] - field[:-2, 1:-1]) / (2 * dx)
            )
        
        return zero_field
    
    elif axis == 1:
       zero_field[1:-1,1:-1]+=(
           (field[1:-1, 2:] - field[1:-1, :-2]) / (2 * dx)
           )
       
       return zero_field
    
def second_derivative(field, axis):
    zero_field = np.zeros_like(field)
    if axis == 0:
        zero_field[1:-1,1:-1]+= (
            (field[2:, 1:-1] + field[:-2, 1:-1] - 2 * field[1:-1, 1:-1]) / dx**2
            )
        return zero_field
    
    elif axis == 1:
        zero_field[1:-1,1:-1]+=(
            (field[1:-1, 2:] + field[1:-1, :-2] - 2 * field[1:-1, 1:-1]) / dx**2
            )
        return zero_field
   
#density[10,10] = bd +2

#velocity_u += (np.random.random(density.shape)-0.5)*1
#velocity_v += (np.random.random(density.shape)-0.5)*1


mask = []
flip = 0
value = 1

for i in range(bright.shape[0]):
    mask.append(value)
    flip += 1
    if(flip > 10):
        flip = 0 
        if value == 1:
            value = 0
        else:value = 1

mask = np.array(mask)
#ink[:50,:50] = 2
def solve(n):
 
    global velocity_v
    global velocity_u
    global heat
    global density
    global ink
    
    if not n%10:
        print(n) 
      
    
    
    for step in range(substeps):
        
        
        
        
        dbx = abs(derivative(bright,0))>0.1
        dby = abs(derivative(bright,1))>0.1

        #density[bright < 0.2] = bd
        #ink[:,0] = mask
        #velocity_u[dbx]*=0
        #velocity_v[dby]*=0
        #ink[bright < 0.2] = 0

        if(n < 400):
            #velocity_v[35:50,0:5] = 0
            #velocity_u[35:50,0:5] = 0
            #density[35:50,0:5] = bd
            #ink[35:50,0:5] = 2
        
            #velocity_v[45:50,0:5] = 1
            #density[45:50,0:5] = bd
            #ink[45:50,0:5] = 2
            pass
        
        heat[-2:,30:50] = 2
        #heat -= (heat-(-0.3))*0.0001
        

        
        #heat[-2:,3:] = 2
 

        dux = derivative(velocity_u, 0)
        duy = derivative(velocity_u, 1)

        d2ux = second_derivative(velocity_u, 0)
        d2uy = second_derivative(velocity_u, 1)

        dvx = derivative(velocity_v, 0)
        dvy = derivative(velocity_v, 1)
        d2vx = second_derivative(velocity_v, 0)
        d2vy = second_derivative(velocity_v, 1)

        ddx = derivative(density, 0)
        ddy = derivative(density, 1)
        d2dx = second_derivative(density, 0)
        d2dy = second_derivative(density, 1)

        dix = derivative(ink, 0)
        diy = derivative(ink, 1)
        d2ix = second_derivative(ink, 0)
        d2iy = second_derivative(ink, 1)

        dtx = derivative(heat, 0)
        dty = derivative(heat, 1)
        d2tx = second_derivative(heat, 0)
        d2ty = second_derivative(heat, 1)


        dut = -(
            dux*velocity_u + duy*velocity_v + 
            ddx - (d2ux+d2uy)*vd 
            - gravity
            )
        
        ddt = -(
            dux*density + dvy*density +
            velocity_u*ddx + velocity_v*ddy -
            (d2dx+d2dy)*dd
        )
        
        
        dvt = -(
            dvx*velocity_u + dvy*velocity_v +
            ddy - (d2vx+d2vy)*vd 
            )
        
        

        dit = -(
            dix*velocity_u+diy*velocity_v-
            (d2ix + d2iy)*id
            )
        
        
        dtt = -(
            dtx*velocity_u*density +  dty*velocity_v*density-
            (d2tx + d2ty)*td
            )
        
        density += (ddt*dt)
        velocity_u += dut*dt
        velocity_v += dvt*dt
        

        ink += dit*dt
        heat += dtt*dt

        velocity_u += heat*t_buoyancy*dt
        
        
        #clear failures:

        
        #constrains
        velocity_u[:,:] = np.clip(velocity_u,vr[0],vr[1])
        velocity_v[:,:] = np.clip(velocity_v,vr[0],vr[1])

        density[:,:] = np.clip(density,dr[0],dr[1])
        ink[:,:] = np.clip(ink,0,2)
        heat[:,:] = np.clip(heat,-2,2)
       
        # Left boundary:
        velocity_u[:, 0] = velocity_u[:, 1]
        velocity_v[:, 0] = 0
        density[:, 0] = bd
        heat[:, 0] = 0
        ink[:, 0] = ink[:, 1]

        #Right boundary:
        velocity_u[:, -1] = velocity_u[:, -2]
        velocity_v[:, -1] = 0
        density[:, -1] = bd
        heat[:, -1] = 0
        ink[:, -1] = ink[:, -2]

        # top boundary:
        velocity_u[0, :] = 0
        velocity_v[0, :] = velocity_v[1,:]
        density[0, :] = density[1, :] 
        heat[0, :] = 0
        ink[0, :] = ink[1, :]

        #bottom boundaries
        velocity_u[-1, :] = 0
        velocity_v[-1, :] = velocity_v[-2,:]
        density[-1, :] = density[-2, :]
        heat[-1, :] = 0
        ink[-1, :] = ink[-2, :]

    
    mag = np.sqrt(velocity_u**2 + velocity_v**2) 
    curl = (duy - dvx)*10
    div = (dux + dvy)*10
    deviation = density - density.mean()
    implot.set_data(heat)

    
     
path = "left_inlet"
gif_path = path + '.gif'
mp4_path = path + '.mp4'
writer = animation.PillowWriter(fps=30,bitrate=400)
print("running")
data = animation.FuncAnimation(figure,solve, frames = 1800, interval = 1)
#plt.show()
print("saving")
data.save(gif_path,writer = writer)
print("done")
from gif_to_mp4 import Converter
Converter(gif_path,mp4_path)