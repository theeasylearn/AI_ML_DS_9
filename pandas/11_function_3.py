import pandas as pd
s = pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f'])
print(s)
print(s.loc['a']) # 1
print(s.loc['c']) # 3
# print(s.loc['x']) #error because there is no such label x 
print(s.iloc[1]) #2 
print(s.iloc[4]) #2 
# print(s.iloc[11]) #error 
print(s.get('a',None))
print(s.get('x','not found '))
