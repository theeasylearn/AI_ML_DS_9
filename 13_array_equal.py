import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

print(np.array_equal(arr1,arr2)) #True 
arr3 = np.array([1, 2, 4])
print(np.array_equal(arr1,arr3)) #False
arr4 = np.array([[1, 2, 3]])
print(np.array_equal(arr1,arr4)) #False because shape is different
print(arr1.shape,arr4.shape)
