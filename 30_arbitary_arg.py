#print hello message to many person using one function:

def say_hello(*names):
    for name in names:
        print("Hello ",name) 

say_hello("Vivek","Deep","Krisha","Ronit")   
    