# hierarchical inheritance 
class MyMath:
    def getPi(self):
        pi = 3.141516
        return pi 
    def getSquare(self,num):
        square = num * num #square is local variable
        return square 

class Circle(MyMath):
    def __init__(self,radius):
        self.radius = radius
    def getArea(self):
        pi = super().getPi()
        square = super().getSquare(self.radius)
        area = pi * square 
        return area 
class Square(MyMath):
    def __init__(self,size):
        self.size = size 
    def getArea(self):
        area = super().getSquare(self.size)
        return area 
    
radius = int(input("Enter radius"))
c1 = Circle(radius)
print("Area of circle ",c1.getArea())

size = int(input("Enter size of square "))
s1 = Square(size)
print("Size of the square ",s1.getArea())