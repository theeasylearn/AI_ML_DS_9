#create python function that generate and return random password of given length 
import string 
import random as rd 
def generatePassword(count):
    letters = string.ascii_lowercase  + string.ascii_uppercase + string.digits + string.punctuation
    #convert it into list 
    my_list = list(letters)

    #shuffle list 
    rd.shuffle(my_list)
    #pick given no of letter 
    size = len(my_list) - 1
    password = [] 
    for i in range(0,count):
        temp = my_list[rd.randint(0,size)]
        password.append(temp)
    return "".join(password)


print(generatePassword(20))
print(generatePassword(10))
print(generatePassword(25))