#example of inheritance 
class Person:
    def walk(self):
        print("I can walk...")
    def talk(self):
        print("I can talk")
    def eat(self):
        print("I can eat")
#inheritance 
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

s1 = Student()
s1.whatICanDo()
s1.walk() #calling parent class method
s1.read() #calling derived class method