import connect as cn 
from datetime import datetime as dt 
#create cursor 
mycursor = cn.database.cursor()

#build sql statement
sql = "insert into trip (title,detail,start_date,days) values (%s,%s,%s,%s)"

#accept input from user 
title = input("Enter trip title")
detail = input("Enter trip detail")
start_date = input("Enter Trip date (DD-MM-YYYY)")
#convert string date into date 
try:
    start_date = dt.strptime(start_date,"%d-%m-%Y")
    days = int(input("Enter trip days"))
    #create list that has 4 values 
    # values = ['Dwarka Trip','Trip to Dwarka and somnath','2026-04-15',5]
    values = [title,detail,start_date,days]
    #run sql statement 
    mycursor.execute(sql,values)
    cn.database.commit() #required to save changes into database 
    print(mycursor.rowcount," Trip Inserted")
except ValueError as e:
    print("invalid date")
