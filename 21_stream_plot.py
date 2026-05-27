import matplotlib.pyplot as plt 
import numpy as np 

#create array 
x = np.linspace(-3,3,10)
y = np.linspace(-3,3,10)

X, Y = np.meshgrid(x,y)
# print(X,Y)
U = -Y 
V = X
plt.streamplot(X,Y,U,V,density=1,color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('stream plot chart')
plt.grid()
plt.show()
