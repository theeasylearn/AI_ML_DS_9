import numpy as np
a = np.array([1, 2, 3])
b = np.array([1, 0, 3])
# Comparing Two Arrays (Element-wise) to compare array make sure it has same shape
print(a == b) 
print(a != b)
print(a > b)
print(a < b)

#Check if All or Any Elements Match
print(np.all(a == b))
print(np.any(a != b))