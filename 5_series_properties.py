import pandas as pd 
#create series
s4 = pd.Series([10,20,30.45,40,50.25],index=['ram','shyam','mohan','geeta','sita'],name='salary')
print(s4)
print(s4.size) #no of values 
print(s4.shape) #size of each dimension (rows and columns)
print(s4.ndim) #no of dimension
print(s4.index) 
print(s4.values)
print(s4.is_unique)
print(s4.hasnans)