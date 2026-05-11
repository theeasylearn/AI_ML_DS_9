import pandas as pd 

#create series without label 
s1 = pd.Series([10,20,30,40.10,50]) 
print(s1)

s2 = pd.Series([10,20,30,40,50],index=['ram','shyam','mohan','sohan','ravi']) 
print(s2)