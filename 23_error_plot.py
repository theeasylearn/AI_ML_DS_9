import matplotlib.pyplot as plt 
import numpy as np 

x = np.arange(0,11)
y = np.sin(x)
y_error = 0.2

plt.errorbar(x,y,y_error,fmt='o',capsize=5,ecolor='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Error bar chart')
plt.grid()
plt.show()