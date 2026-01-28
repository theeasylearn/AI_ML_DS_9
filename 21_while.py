'''Qs:4 write a program to findout reverse of given no 
    input : 1234 
    output : 4321
    
    12321
    12321
    steps 
    -----------------------
    1   create variable number,reminder,reverse = 0 
    2   accept input from user into number (assume 1234)
    
    3   reminder(4) = number % 10 
    4   reverse(4) = (reverse * 10 )+ reminder
    5   number(123) = number // 10
    
    6   reminder(3) = number % 10 
    7   reverse(43) = (reverse * 10)+ reminder   
    8    number(12) = number // 10
    
    9   reminder(2) = number % 10 
    10   reverse(432) = (reverse * 10)+ reminder
    11    number(1) = number // 10
    
    12   reminder(1) = number % 10 
    13   reverse(4321) = (reverse * 10) + reminder
    
'''

number=int(input("Enter the number to reverse: "))
reverse=0
reminder=0
while number>0:
    reminder=number%10
    reverse=reverse*10+reminder
    number=number//10
print(reverse)
    