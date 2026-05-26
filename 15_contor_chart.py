import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd

# 
data = pd.read_csv('mount_everest_temperature_contour_data.csv').squeeze()
print(data)
# plt.show()

grid_size = int(np.sqrt(len(data)))
#convert 1d Series into 2d dataframe
X = data['Longitude_deg'].values.reshape(grid_size, grid_size)
Y = data['Latitude_deg'].values.reshape(grid_size, grid_size)
Z = data['Temperature_C'].values.reshape(grid_size, grid_size)

plt.figure(figsize=(8, 6))
contour = plt.contour(X, Y, Z, levels=20, cmap='RdYlBu_r')
colorbar = plt.colorbar(contour)
plt.contour(X,Y,Z,level=10,color='black')
plt.show()