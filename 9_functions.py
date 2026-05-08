import pandas as pd 

data = [1,2,2,3,3,3,4,None]

#convert series 
s1 = pd.Series(data)
print(s1)

print(s1.mode())
print(s1.std())
print(s1.var())
print(s1.count())
print(s1.isnull())
print(s1.notnull())
print(s1.dropna())
print(s1.fillna(value=0))