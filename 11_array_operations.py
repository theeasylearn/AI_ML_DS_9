import numpy as np
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

#maths operation
print("Addition ",a+b)
print("multiplication ",a*b)
print("subtraction ",a-b)
print("division ",a/b)

#scaler operation 
print("adding 1 to each and every value ",a+1)
print("subtract 2 to each and every value ",a-2)
print("multiply 3 to each and every value ",a*3)
print("division 4 to each and every value ",a/4)

print("square root of each and every value",np.sqrt(a))
print("sin value each and every value",np.sin(a))
print("cos value each and every value",np.cos(a))
print("tan value each and every value",np.tan(a))
print("exponential value each and every value",np.exp(a))


#comparison operator
print(a>15)
print(a==20)
print(a!=100)
print(a>80)

print("matrix multiplication")
print(a @ b)
print(np.dot(a,b))