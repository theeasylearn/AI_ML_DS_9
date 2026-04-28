class Society:
    #class variable
    enrollment_no = 0
    def __init__(self,name,flatno,tower):
        # increase enrollment no 
        Society.enrollment_no += 1
        self.name = name 
        self.flatno = flatno
        self.tower = tower 
        self.no = Society.enrollment_no #1
        print("constructor called...")
    def display(self):
        print(f"No = {self.no} Name = {self.name} tower = {self.tower} flatno = {self.flatno}")

s1 = Society('Ankit Patel','champa',104)
s1.display()
print(s1.name,s1.tower,s1.flatno)

s2 = Society('Niket Mehta','champa',202)
s2.display()

s3 = Society('sandeep parmar','dollar',401)
s3.display()
print("Last enrollment no ",Society.enrollment_no)
