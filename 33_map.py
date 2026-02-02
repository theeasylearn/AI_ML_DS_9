#map(function, iterable, ...)

numbers=[1,2,3,4,5,6,7]

res=list(map(lambda num:num*num ,numbers))
print(res)

tup=(1,2,3,4,5)
res1=list(map(lambda n:n+1 ,tup))
print(res1)

num1=[1,2,3]
num2=[10,20,30]
res2=list(map(lambda x,y:x+y ,num1,num2))
print(res2)