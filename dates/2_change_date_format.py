from datetime import datetime as dt 
birthdate = input("Enter your birthdate (dd-mm-YYYY)")
print(birthdate)
#convert it into date 
birthdate = dt.strptime(birthdate,"%d-%m-%Y")
print(birthdate)
#convert & display date one format to another format  (usa format) 
print(birthdate.strftime('%a %m-%d-%Y')) #%a Abbreviated weekday name (Sun, Mon, Tue)