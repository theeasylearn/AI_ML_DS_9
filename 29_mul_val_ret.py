# function that returns multiple values for addition ,subtraction ,multiplication and division

def equation(num1,num2):
    addition=num1+num2
    subtraction=num2-num1
    multiplication=num1*num2
    division=num2/num1
    
    return addition,subtraction,multiplication,division

x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))

result=equation(x,y)
print(result)