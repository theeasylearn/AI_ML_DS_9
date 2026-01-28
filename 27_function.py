#def func_name(args):
    #statements
    
#without arg without return value

def pythagoras():
    a=int(input("Entrt the number: "))
    b=int(input("Entrt the number: "))
    
    res=a**2+b**2
    c=res**0.5
    print("c=",c)

pythagoras()

#Without return value with argument

def pythagoras(a,b):
    res=a**2+b**2
    c=res**0.5
    print("c=",c)

a=int(input("Entrt the number: "))
b=int(input("Entrt the number: "))
pythagoras(a,b)

#With return value without argument

def pythagoras():
     a=int(input("Entrt the number: "))
     b=int(input("Entrt the number: "))
     res=a**2+b**2
     res1=res**0.5
     return res1
c=pythagoras()
print("c=",c)

#With return value with argument

def pythagoras(a,b):
    res=a**2+b**2
    res1=res**0.5
    return res1

a=int(input("Entrt the number: "))
b=int(input("Entrt the number: "))
c=pythagoras(a,b)
print("c=",c)