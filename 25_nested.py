'''
Qs:1 write a program to print following pattern (only one astrik at time will be displayed)

*
* *
* * *
* * * *
* * * * *
'''

for i in range(1,6):
    for j in range(i):
        print("*",end='')
    print(" ")
    
row = 1
while row<=5: #outer loop
    column=1
    while column<=row: #inner loop 
        print('*',end=' ')
        column=column+1
    print(" ") #new line 
    row=row+1
