#lambda arguments: expression

add=lambda a,b:a+b
sub=lambda a,b:a-b
multi=lambda a,b:a*b
div=lambda a,b:a/b
square=lambda a:a*a

a=int(input("Enter the number: "))
b=int(input("Enter the number: "))

print(add(a,b))
print(sub(a,b))
print(multi(a,b))
print(div(a,b))
print(square(a))