import numpy as np 

#create an array 
array_1 = np.arange(1,11)
print(array_1)

array_2 = np.copy(array_1)
print(array_2)

list = [25,50,100,200,500]
#copy list as array 
array_3 = np.copy(list)
print(array_3)

tuple = (100,50,200,150,300,200)
#copy tuple as array 
array_4 = np.copy(tuple)
print(array_4)
