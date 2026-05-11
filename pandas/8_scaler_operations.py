import pandas as pd 

data = [10,20,30,40,100,125]

#convert series 
s1 = pd.Series(data)
print("Original value ",s1)


print("after adding 2 into each value",s1.add(2))

print("after subtracting 5 from each ",s1.sub(5))


print("after multiplying each value with 2",s1.mul(2))

print("after dividing each value by 3",s1.div(3))
print("sum of all values ",s1.sum())
print("mean of all values ",s1.mean())
print("median of all values ",s1.median())

