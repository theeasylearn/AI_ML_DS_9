import connect as cn 
from datetime import datetime as dt 
try:
    #create cursor object
    mycursor = cn.database.cursor()

    #create sql statement 
    sql = "update trip set title=%s,detail=%s,start_date=%s,days=%s where id=%s"

    #create variable & accept input
    title = input("Enter new trip title")
    detail = input("Enter new trip detail")
    start_date = input("Enter new start date (DD-MM-YYYY)")
    start_date = dt.strptime(start_date,"%d-%m-%Y")
    days = int(input("Enter revised trip days"))
    id = int(input("Enter trip id to update"))

    #create list 
    values = [title,detail,start_date,days,id]

    #execute sql statement
    mycursor.execute(sql,values)

    cn.database.commit()
except ValueError as Error:
    print("invalid date")
else:
    print(mycursor.rowcount, " trip updated")
finally:
    print("good bye.")