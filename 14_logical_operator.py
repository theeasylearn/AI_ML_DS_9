import numpy as np
arr1 = np.array([1, 2, 3, -1, 5])
arr2 = np.array([4, 0, 2, 7, 9])

print(arr1,arr2) 

#logical and 
print(np.logical_and(arr1>0,arr2<5))

#logical or
print(np.logical_or(arr1>0,arr2<5))

#logical not 
#logical and 
print(np.logical_not(arr1>0))

print(np.logical_xor(arr1>0,arr2<5))

