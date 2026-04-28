# multi level inheritance 
class KG:
    def __init__(self,grams):
        self.grams = grams
        print("KG class constructor run...")
    def getKG(self):
        #here kg local variable
        kg = self.grams / 1000
        return kg 
#derived/child class
class Quintal(KG):
    def  __init__(self, grams):
        super().__init__(grams)
        print("Quintal function called")
    def getQuintal(self):
        kg = super().getKG()
        temp = kg / 1000 
        return temp
#leaf class 
class Ton(Quintal):
    def __init__(self, grams):
        super().__init__(grams) #calling parent class constructor
        print("Ton class constructor called")
    def getTon(self):
        Quintal = super().getQuintal()
        ton = Quintal / 10
        return ton 
    
grams = int(input("Enter grams"))
t1 = Ton(grams)
print("ton = ",t1.getTon())
    
