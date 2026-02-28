#example of inheritance (multiple level)
class Animal:
    def hunt(self):
        print("I can hunt")
    def sleep(self):
        print("I can sleep")
    def run(self):
        print("I can run")

class Bird:
    def fly(self):
        print("I can fly")
    def sing(self):
        print("I can sing")

class Unicorn(Animal,Bird):
    def speak(self):
        print("I can speak")
    def fire(self):
        print("I can fire")
    def whatICanDo(self):
        super().hunt()
        super().run()
        super().sleep()
        super().fly()
        super().sing()
        self.speak()
        self.fire()

u1 = Unicorn()
u1.whatICanDo()