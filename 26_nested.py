'''
Qs:2 write a program to print following pattern
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
'''

#row=5
# while row>=1:
#     column=1
#     while column<=row:
#         print(f'{column} ',end=' ')
#         column=column+1
#     print('') #new line
#     row=row-1
 
count=1   
for i in range(5,0,-1) :
    for j in range(i):
        print(count,end='')
        count+=1       
    count=1
    print(" ")