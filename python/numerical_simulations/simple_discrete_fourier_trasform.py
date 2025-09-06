import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0,10, 1000)
data = (abs(time - 5) < 5)*2



def forward(data:np.ndarray,time:np.ndarray):


    frequecies = []
    for f in np.linspace(0,100,1000):
        a = (np.sin(time*f)*data).mean() 
        b = (np.cos(time*f)*data).mean()
        frequecies.append([f,a,b])
    return frequecies




def view_forward(time,frequencies):
    data = np.zeros_like(time)
    for i in frequencies:
        data += i[1]*np.sin(time*i[0])
        data += i[2]*np.cos(time*i[0])
    return data



#plt.plot(time,data)


frequencies = np.array(forward(data, time))
plt.plot(frequencies[:][0], frequencies[:][1])
plt.plot(frequencies[:][0], frequencies[:][2])
plt.show()
