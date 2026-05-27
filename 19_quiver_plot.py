import matplotlib.pyplot as plt 
import numpy as np 

#create array 
x = np.linspace(-3,3,10)
y = np.linspace(-3,3,10)

X, Y = np.meshgrid(x,y)
# print(X,Y)
U = -Y 
V = X
plt.quiver(X,Y,U,V,color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Quiver plot chart')
plt.grid()
plt.show()
