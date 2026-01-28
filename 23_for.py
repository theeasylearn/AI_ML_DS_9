#Qs:1 write a program to count vowels in given string (a e i o u A E I O U) 

str="i am a student"

count=0
for character in str:
    if character=='a' or character=='e' or character=='i' or character=='o' or character=='u' or character=='A' or character=='E' or character=='I' or character=='O' or character=='U':
        count+=1
print("Total number of vowels in a string: ",count)


#Qs:2 print 1 to 10 using for loop 
#range(initial,final+1,increment(default)/decrement)

for i in range(1,11):
    print(i)


#Qs:3 count even number between 1 t0 10

count=0
for i in range(1,11):
    if i%2==0:
        count+=1
print(count)