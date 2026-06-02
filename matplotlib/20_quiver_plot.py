import matplotlib.pyplot as plt 
import numpy as np 

# 1. Establish Precision Environment & Base Constraints
np.random.seed(42)
num_vehicles = 100

# Central coordinate anchor for Ahmedabad layout
base_lat = 23.0225
base_lon = 72.5714

# 2. Simulate Spatial Distribution (X, Y) Scaler operation
lons = base_lon + np.random.uniform(-0.05, 0.05, num_vehicles)
lats = base_lat + np.random.uniform(-0.05, 0.05, num_vehicles)

# 3. Formulate Directional Delta Vectors (U, V)
u_vectors = np.random.uniform(-0.006, 0.006, num_vehicles)
v_vectors = np.random.uniform(-0.006, 0.006, num_vehicles)

plt.quiver(lons,lats,u_vectors,v_vectors,color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Quiver plot chart')
plt.grid()
plt.show()