import pandas as pd 

data = [1,2,2,3,3,3,4,None]

s1 = pd.Series(data)
print(s1.duplicated())

s1.drop_duplicates(inplace=True)
print(s1)
s1 = s1.replace(3.0,5.0)
print(s1)

s1 = s1.clip(1.0,3.0)
print(s1)
s1 = s1.dropna()
print(s1)

print(s1.cumsum())
print(s1.cumprod())