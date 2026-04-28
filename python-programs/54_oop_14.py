class Account:
    def __init__(self,name,acctype,balance):
        #public variable 
        self.name = name 
        self.acctype = acctype
        #private variable
        self.__balance = balance 
    def display(self):
        print(self.name,self.acctype, self.__balance)

    def updateBalance(self,amount):
        self.__balance = self.__balance + amount 

a1 = Account("Ronit","savings",525000)
a1.display()
a1.__balance = 1250000 #this is ignored to avoid accidental changes 
a1.updateBalance(99)
a1.display()
