#concept of instance variable and constructor 
class Human:
    #constructor (called automatically & used to create instance variable)
    def __init__(self,name,surname,gender):
        #instance variable (is create using self keyword)
        self.name = name 
        self.surname = surname
        self.gender = gender
        print("constructor called....")
    def getPrifix(self):
        temp = None #local variable
        if self.gender == True:
            temp = "Mr. "
        else:
            temp = "Miss/Mrs"
        return temp 
    def walk(self):
        temp = self.getPrifix() #calling member function of same class 
        print(f"{temp} {self.name} {self.surname} can walk")
    def talk(self):
        temp = self.getPrifix()
        print(f"{temp} {self.name} {self.surname} can talk")
    def sleep(self):
        temp = self.getPrifix()
        print(f"{temp} {self.name} {self.surname} can sleep")

#create object
ronit = Human("Ronit","Solanki",True) #it will automatically(implictly) call constructor
ronit.walk()
ronit.talk()
ronit.sleep()

#create another object
name = input("Enter name")
surname = input("Enter surname")
diya = Human(name,surname,gender=False)
diya.sleep()
diya.walk()
diya.talk()

