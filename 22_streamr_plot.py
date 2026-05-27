import matplotlib.pyplot as plt 
import numpy as np 

# 1. Establish Precision Environment & Base Constraints
np.random.seed(42)
num_vehicles = 100

# Central coordinate anchor for Ahmedabad layout
base_lat = 23.0225
base_lon = 72.5714

# 2. Simulate Spatial Distribution (X, Y) Scaler operation
lons = base_lon + np.linspace(0.01, 0.05, num_vehicles)
lats = base_lat + np.linspace(0.01, 0.05, num_vehicles)

X, Y = np.meshgrid(lons,lats)   # This is the key step!

# 3. Formulate Directional Delta Vectors (U, V)
u_vectors =  Y 
v_vectors = - X

plt.streamplot(lons,lats,u_vectors,v_vectors,density=1,color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('stream plot chart')
plt.grid()
plt.show()