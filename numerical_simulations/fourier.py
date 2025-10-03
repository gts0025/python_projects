
import numpy as np

def forward(data:np.ndarray,time:np.ndarray,f_range:list = [0,1000], samples:int = 1000):


    frequecies = []
    n = time.shape[0]
    for f in np.linspace(f_range[0],f_range[1],samples):
        a = (np.sin(2*np.pi*f*time) * data).sum() / n
        b = (np.cos(2*np.pi*f*time) * data).sum() / n
        frequecies.append([f,a,b])
    return frequecies




def inverse(time,frequencies):
    data = np.zeros_like(time)
    for f,a,b in frequencies:
        data += a*np.sin(2*np.pi*f*time)
        data += b*np.cos(2*np.pi*f*time)
    return data


def fourier_derivative(time,frequencies):
    data = np.zeros_like(time)
    for f,a,b in frequencies:
        data += (2*np.pi*f) * a * np.cos(2*np.pi*f*time)
        data -= (2*np.pi*f) * b * np.sin(2*np.pi*f*time)
    return data



