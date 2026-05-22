import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(0,10,100)
# print(x)
y = np.sin(x) 
# print(y)
plt.fill_between(x,y,label=y)
plt.title("area plot chart")
plt.xlabel("X")
plt.ylabel("y")
plt.show()

