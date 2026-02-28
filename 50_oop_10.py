# single level inheritance 
class KG:
    def __init__(self,grams):
        self.grams = grams
        print("KG class constructor run...")
    def getKG(self):
        #here kg local variable
        kg = self.grams / 1000
        return kg 
class Quintal(KG):
    def  __init__(self, grams):
        super().__init__(grams)
        print("Quintal function called")
    def getQuintal(self):
        kg = super().getKG()
        temp = kg / 1000 
        return temp 
    
k1 = KG(10000)
kg = k1.getKG()
print("KG ",kg)

q1 = Quintal(100000000000000)
temp = q1.getQuintal()
print("Quintal ",temp)

