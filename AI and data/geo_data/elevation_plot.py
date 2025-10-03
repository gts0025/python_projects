import rasterio
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np



batfilename = "mountains.tif"

with rasterio.open(batfilename) as src:
    bat_elevation = src.read(1)          # Read the first band (e.g., elevation)
    bat_bounds = src.bounds              # Geographic extent
    bat_crs = src.crs                    # CRS info (WGS84/EPSG:4326)

print(bat_bounds)


# Assuming bat_elevation is a 2D numpy array
shape = bat_elevation.shape
ny, nx = shape  # rows (y), cols (x)

x = np.linspace(bat_bounds.left,bat_bounds.right,nx)   # columns
y = np.linspace(bat_bounds.bottom,bat_bounds.top,ny) 
x, y = np.meshgrid(x, y)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(projection="3d")

# Plot surface
ax.plot_surface(x, y, bat_elevation, cmap="jet")

ax.set_xlabel("X (pixel)")
ax.set_ylabel("Y (pixel)")
ax.set_zlabel("Elevation (m)")
plt.title("3D Terrain Surface")
plt.show()
