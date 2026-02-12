name = input("What is your full name")
print(name) 
print(name.lower())
print(name.upper())
print("is this name variable has only alphabets ",name.isalpha())
print("is this name variable has only lower case alphabets ",name.islower())
print("is this name variable has only upper case alphabets ",name.isupper())
print("is this name variable has only title case alphabets ",name.istitle())
print("is this name variable has only digits  ",name.isnumeric())
print("is this name variable has only space  ",name.isspace())
print(len(name))

fruits = ["apple","banana","mango","pineapple","graps"] 
print(fruits)
#convert it into string but separated by space 
line = " "
print(line.join(fruits)) # apple,banana,mango,pineapple,graps
alphabets = "a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9"
print(alphabets)
list = alphabets.split()
print(list)

sentence = "India is a country where India’s diversity, India’s culture, India’s history, and India’s unity are celebrated"
print(sentence)
print(sentence.replace('India','Bharat'))
print(sentence.replace('India','Bharat',1)) #only 1st occurrence will be replaced