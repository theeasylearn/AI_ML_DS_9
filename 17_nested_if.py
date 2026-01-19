age=int(input("Enter your age: "))
voter_id=input("Do ypu have your voter id? : ")
nationality=input("What is your nationality? : ")


if nationality=='Indian' or nationality=='INDIAN' or nationality=='indian':
    print("You can move further")
    if age>=18:
        print("You can move further")
        if voter_id=='YES' or voter_id=='yes' or voter_id=='Yes':
            print("You can go for votting")
        else:
            print("voter id is must for votting")    
    else:
        print("Your age should be greater than 18")
else:
    print("sorry you are not eligible for votting...")
     