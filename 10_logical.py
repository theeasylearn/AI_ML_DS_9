a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
c=int(input("Enter the number: "))

print(a==b and b==c)
print(a>=c and a==b)
print(a!=b and c>=b)
print(b>=c and c>=a)

print(a==b or b==c)
print(a>=c or a==b)
print(a!=b or c>=b)
print(b>=c or c>=a)

print(not(a==b and b==c))
print(not(a>=c or a==b))
print(not(a!=b and c>=b))
print(not(b>=c or c>=a))