#example of inheritance (hybrid level)
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

class Actor(Person):
    def dance(self):
        print("I can dance")
    def acting(self):
        print("I can act")
    def whatICanDo(self):
        super().walk()
        super().talk()
        super().eat()
        self.dance()
        self.acting()

class Robot(Student,Actor):
    def analyze(self):
        print("I can analyze situation")
    def fight(self):
        print("I can fight")
    def whatICanDo(self):
        Student.whatICanDo(self)
        Actor.whatICanDo(self)
        self.analyze()
        self.fight()
r1 = Robot()
r1.whatICanDo()
