import numpy as np 
import matplotlib.pyplot as plt 
#create an array 
marks = np.random.randint(40,100,1000)

# print(len(marks))
plt.hist(marks,bins=6,density=True,color='blue',label='Marks')
plt.xlabel('marks')
plt.ylabel('Density')
plt.title("Student Performance")
plt.legend()
plt.grid()
plt.show()

