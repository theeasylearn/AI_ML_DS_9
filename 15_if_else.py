math=int(input("Enter your maths marks: "))
eng=int(input("Enter your english marks: "))
sci=int(input("Enter your science marks: "))

total=math+eng+sci
percentage=total/3

print("---------------Result---------------")
print("Maths:",math)
print("English:",eng)
print("Science:",sci)
print("Total:",total)
print("Percentage: ",percentage,"%")
if percentage>=80:
    print("Very good!")
    
if percentage>=40 and percentage<80:
    print("Good")
    
if percentage<40:
    print("poor")
else:
    print("Good Bye")
    