x=10
y=10

print(x is y)
print(x is not y)

lit=[1,2,3,4,5]
print("Id of list before change: ",id(lit))
lit.append(6)
print(lit)
print("Id of list after change: ",id(lit))

str="I am a student"
print("Id of string before change: ",id(str))

str=str+ "i am learning python"
print("Id of list after change: ",id(str))