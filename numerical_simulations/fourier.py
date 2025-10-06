
import numpy as np
from numba import njit

@njit(fastmath=True, parallel=True)

def forward(data, time, f_range=np.array([0,1000]), samples=1000):
    n = time.shape[0]
    result = np.zeros((samples, 3), dtype=np.float64)
    freqs = np.linspace(f_range[0], f_range[1], samples)
    for i in np.arange(samples):
        f = freqs[i]
        s = np.sin(2*np.pi*f*time)
        c = np.cos(2*np.pi*f*time)
        result[i,1] = 2/n * (s*data).sum()
        result[i,2] = 2/n * (c*data).sum()
        result[i,0] = f
    return result


@njit(fastmath=True, parallel=True)
def inverse(time, frequencies):
    data = np.zeros_like(time)
    n_freq = frequencies.shape[0]
    
    for i in np.arange(n_freq):
        f, a, b = frequencies[i]
        data += a*np.sin(2*np.pi*f*time)
        data += b*np.cos(2*np.pi*f*time)
    return data


@njit(fastmath=True, parallel=True)
def fourier_derivative(time,frequencies):
    data = np.zeros_like(time)
    n_freq = frequencies.shape[0]
    
    for i in np.arange(n_freq):
        f, a, b = frequencies[i]
        data += (2*np.pi*f) * a * np.cos(2*np.pi*f*time)
        data -= (2*np.pi*f) * b * np.sin(2*np.pi*f*time)
    return data



