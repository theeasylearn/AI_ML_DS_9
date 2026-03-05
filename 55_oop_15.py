#method overloading 

class Area:
    def getArea(self,length=0,width=0):
        if length ==0 and width ==0:
            return 1
        elif length != 0:
            return length * length
        elif width != 0:
            return width * width
        else: 
            return length * width
a1 = Area()
print(a1.getArea()) # 1
print(a1.getArea(10)) # 1
print(a1.getArea(10,20)) # 1