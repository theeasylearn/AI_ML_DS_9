import numpy as np 

list = [[
            [10,20,30],
            [40,50,60],
            [70,80,90]
        ],
        [
            [110,220,230],
            [140,150,160],
            [170,180,190]
        ]
       ]

#convert into array
array_3d = np.copy(list)
print(array_3d)
print("Dimension ",array_3d.ndim)
print("Shape ",array_3d.shape)
print("Size ",array_3d.size)
print("size of each element",array_3d.itemsize)
print("data type of array",array_3d.dtype)
print("Total size of array ",array_3d.nbytes)