import connect as cn 
from datetime import datetime as dt 
mycursor = cn.database.cursor(dictionary=True)
print("Press 1 to transaction management")
print("Press 2 to trip management")
print("Press 0 to exit from program")
choice = int(input("Enter your choice"))
if choice<0 or choice>2:
    print("invalid choice")
elif choice==1:
    print("Transaction management")
    print("Press 1 to display transaction")
    print("Press 2 to add new transaction")
    print("Press 3 to update existing transaction")
    print("Press 4 to delete existing transaction")
    print("Press 0 to exit")
    transaction_choice = int(input("Enter transaction choice"))
    if transaction_choice<0 or transaction_choice>4:
        print("Invalid transaction choice")
    # elif transaction_choice==1:
    # elif transaction_choice==2:
    # elif transaction_choice==3:
    # elif transaction_choice==4:
    # else:
    #     print("good bye")

elif choice==2:
    while True:    
        print("Press 1 to display trip")
        print("Press 2 to add new trip")
        print("Press 3 to update existing trip")
        print("Press 4 to delete existing trip")
        print("Press 0 to exit")
        trip_choice = int(input("Enter trip choice"))
        if trip_choice<0 or trip_choice>4:
            print("Invalid trip choice")
        elif trip_choice==1:
            #create sql statement
            sql = "select id,title,detail,date_format(start_date,'%d-%m-%Y') as start_date ,days from trip order by id desc";

            #run sql statement
            mycursor.execute(sql) 

            #fetch one row 
            # firstrow = mycursor.fetchone()
            # print(firstrow)

            #fetch all rows 
            table = mycursor.fetchall()

            #display 
            # print(table)
            print(f"{'id':<10} {'title':<32} {'detail':<32} {'start date'} {'':<18} {'days':<10}")
            print("_"*112)
            for row in table:
                print(f"{row['id']:<10} {row['title']:<32} {row['detail']:<32} {row['start_date']} {'':<12} {row['days']:10}")
        elif trip_choice==2:
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
        elif trip_choice==3:
            try:
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
        elif trip_choice==4:
            sql = "delete from trip where id=%s"
            id = int(input("Enter trip id to delete"))
            values = [id]
            mycursor.execute(sql,values)
            cn.database.commit()
            print(mycursor.rowcount, " trip deleted")
        else:
            print("good bye.") 
            break # loop break(stop)
        key = input("Press enter to continue")    