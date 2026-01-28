#write a function for => (x+y)**2=x**2+2*x*y+y**2

def getsquare(x,y=3):
    square=x**2+2*x*y+y**2
    return square

x=5
ans=getsquare(x)
print(ans)