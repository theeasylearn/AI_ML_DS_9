# multiple inheritance & hybrid inheritance 
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

class MyProperty(Circle,Square):
    def __init__(self, radius,size):
        Circle.__init__(self,radius)
        Square.__init__(self,size)
    def getTotalArea(self):
        total = Circle.getArea(self) + Square.getArea(self)
        return total 
    
radius = int(input("Enter radius"))
size = int(input("Enter size of square "))
m1 = MyProperty(radius,size)
print("Total area of my property = ",m1.getTotalArea())

