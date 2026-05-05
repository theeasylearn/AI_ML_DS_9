import numpy as np 

list = [[10,20,30],[40,50,60],[70,80,90]]

#convert into array
array_2d = np.copy(list)
print(array_2d)
print("Dimension ",array_2d.ndim)
print("Shape ",array_2d.shape)
print("Size ",array_2d.size)
print("size of each element",array_2d.itemsize)
print("data type of array",array_2d.dtype)
print("Total size of array ",array_2d.nbytes)

