#filter(function, iterable)

lit=[1,2,3,4,5,6,7]

even=list(filter(lambda a:a%2==0 , lit))
print(even)