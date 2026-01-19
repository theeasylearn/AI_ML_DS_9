num1=int(input("Enter the number :"))
num2=int(input("Enter the number :"))
num3=int(input("Enter the number :"))

if (num1>=num2) and (num1>=num3) :
    print(num1," is maximum number")
elif (num2>=num3) and (num2>=num1):
    print(num2," is the maximum number")
else:
    print(num3," is maximum number")
    