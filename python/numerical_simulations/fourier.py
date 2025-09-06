
import numpy as np

time = np.linspace(0,10, 1000)
data = (abs(time - 5) < 2)*2

def forward(data:np.ndarray,time:np.ndarray,f_range:list = [0,1000], samples:int = 1000):


    frequecies = []
    for f in np.linspace(f_range[0],f_range[1],10000):
        a = (np.sin(time*f)*data).mean() 
        b = (np.cos(time*f)*data).mean()
        frequecies.append([f,a,b])
    return frequecies




def inverse(time,frequencies):
    data = np.zeros_like(time)
    for i in frequencies:
        data += i[1]*np.sin(time*i[0])
        data += i[2]*np.cos(time*i[0])
    return data

