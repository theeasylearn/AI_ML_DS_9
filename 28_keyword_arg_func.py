#Get merit of 5 subject using keyword argument:

def merit(maths,english,science,gujarati,hindi):
    total=maths+english+science+gujarati+hindi
    print("Total marks: ",total)
    
maths=int(input("Enter the maths marks: "))
english=int(input("Enter the english marks: "))
science=int(input("Enter the science marks: "))
gujarati=int(input("Enter the gujarati marks: "))
hindi=int(input("Enter the hindi marks: "))

merit(hindi=hindi,gujarati=gujarati,science=science,english=english,maths=maths)