import numpy as np
print("Numpy version",np.__version__)
numbers = [7, 23, 91, 14, 56]
matrix = [[4, 12, 7], [9, 3, 15]]
#create 1d array 
array_1d = np.array(numbers)
#create 2d array
array_2d = np.array(matrix)
print("1 dimensional array ")
print(array_1d)
print("2 dimensional array ")
print(array_2d)
mixed_list = [10, 3.5, 7, 2.8, 15]

#convert into array
float_array = np.array(mixed_list)
print(float_array)