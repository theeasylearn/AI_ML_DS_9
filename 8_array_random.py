import numpy as np 

#create array of size 3 row and 4 column with random value 

array_1 = np.random.random([3,4])
print(array_1)

#create 1d array of float type of size 5
array_2 = np.random.uniform(10,100,size=5)
print(array_2)

#create 1d array of integer type of size 5 value in range of 10 to 100
array_3 = np.random.randint(10,100,size=5)
print(array_3)

#pick any one value from array_3 randomly
print(np.random.choice(array_3))

#change position of all values in array randomly 
np.random.shuffle(array_3)
print(array_3)

