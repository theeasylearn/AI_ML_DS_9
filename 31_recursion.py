#Qs:1 fibbonacci:

def fibbo(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibbo(num-1)+fibbo(num-2)
    
num=5
for i in range(num):
    print(fibbo(i))

    
#Qs:2 factorial:

def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)
    
num=5
res=fact(num)
print(res)