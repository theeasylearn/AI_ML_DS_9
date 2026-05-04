import numpy as np
arr = np.array([[10, 20, 30], [40, 50, 60]])
print(arr)

#access 1st column of each and every row 
print(arr[:,0]) #here : means any 

#access all column of 1st row
print(arr[0,:]) #here : means any 

#array filtering 

#access all values above 40
print(arr[arr>40])

#access all values below 30 (filtering)
print(arr[arr<30])
