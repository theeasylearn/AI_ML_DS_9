#example of inheritance (multi level)
class Person:
    def walk(self):
        print("I can walk...")
    def talk(self):
        print("I can talk")
    def eat(self):
        print("I can eat")
#inheritance 
#derived class
class Student(Person):
    def read(self):
        print("I can read")
    def write(self):
        print("I can write")
    
    def whatICanDo(self):
        super().walk()
        super().talk()
        super().eat()
        self.read()
        self.write()

# leaf class 
class Developer(Student):
    def code(self):
        print("i can write code in python")
    def debug(self):
        print("i can debug code in python")
    #method overidding 
    def whatICanDo(self):
        super().whatICanDo() #calling parent class method

s1 = Student()
s1.whatICanDo() #student's class method will be called 

d1 = Developer()
d1.whatICanDo() #developer class what i can do method will be called


