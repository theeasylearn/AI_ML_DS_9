'''Qs:2 write a program to print following pattern 
    2   4   6   8   10  12  .....   100
    steps 
    ----------------------------------
    1)  create variable number 
    2)  store 2 into number
    3)  print number 
    4)  number(4) = number + 2 
    5)  print number
    6)  number(6) = number + 2 
    7)  print number
    
2 4 6 
'''

num=2
while num<=100:
    print(num,end=' ')
    num+=2