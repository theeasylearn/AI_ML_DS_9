import connect as cn 
from datetime import datetime as dt

tourid = 0 #global variable
transaction_id = 0 #global variable
mycursor = cn.database.cursor(dictionary=True)
def DisplayTour(isDeleted=0):
    #create sql statement
    if isDeleted == 0:
        sql = "select id,title,detail,date_format(start_date,'%d-%m-%Y') as start_date ,days from trip where isdeleted=0 order by id desc";
    else:
        sql = "select id,title,detail,date_format(start_date,'%d-%m-%Y') as start_date ,days from trip order by id desc";
    #run sql statement
    values = [isDeleted]
    mycursor.execute(sql,isDeleted) 

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
def FetchTourId():
    DisplayTour(1)
    global tourid
    tourid = int(input("Enter tour id"))
    sql = "select id from trip where id=%s"
    values = [tourid]
    mycursor.execute(sql,values)
    table = mycursor.fetchall()
    return table 
def DisplayTransaction():
    table = FetchTourId()
    if len(table)==0:
        print("trip id not found")
    else:
        print("fetch all transaction of given tour")
        sql = "select id, amount, flag, description, challanno, date_format(trandate,'%a %d-%m-%Y') as trandate from transactions where tourid=%s"
        values = [tourid]
        mycursor.execute(sql,values)
        table = mycursor.fetchall()
        print(f"{'id':<5} {'tran date':<15} {'description':<58} {'flag':<2} {'':9}{'amount'} {'ch.no':12}")
        print("_"*110)
        msg = None
        income = expense = 0 # chain assignment
        for row in table:
            if row['flag'] == 1:
                msg='inc'
                income += row['amount']
            else:
                msg='Exp'
                expense+= row['amount']
            print(f"{row['id']:<5} {row['trandate']:<15} {row['description']:<60} {msg:<2} {row['amount']:14} {row['challanno']:12}")
        
        print("_"*110)
        temp = None 
        if income>expense:
            temp = "Profit Amount"
        else: 
            temp = "Loss Amount"

        print(f"Total expense =  {expense}       Total Income {income}              {temp} {income-expense}")
        print("_"*110)
def FetchTransactionId():
    global transaction_id
    DisplayTransaction()
    transaction_id = int(input("Enter transaction id"))
    sql = "select id from transactions where id=%s"
    values = [transaction_id]
    mycursor.execute(sql,values)
    table = mycursor.fetchall()
    return table 
while True:
    print("Press 1 to transaction management")
    print("Press 2 to trip management")
    print("Press 0 to exit from program")
    choice = int(input("Enter your choice"))
    if choice<0 or choice>2:
        print("invalid choice")
    elif choice==1:
        while True:
            print("Transaction management")
            print("Press 1 to display transaction")
            print("Press 2 to add new transaction")
            print("Press 3 to update existing transaction")
            print("Press 4 to delete existing transaction")
            print("Press 0 to exit")
            transaction_choice = int(input("Enter transaction choice"))
            if transaction_choice<0 or transaction_choice>4:
                print("Invalid transaction choice")
            elif transaction_choice==1:
               DisplayTransaction()
            elif transaction_choice==2:
                table = FetchTourId()
                if len(table)==0:
                    print("trip id not found")
                else:
                    sql = "insert into transactions (tourid,amount,flag,description,challanno,trandate) values (%s,%s,%s,%s,%s,%s)"
                    try:
                        amount = int(input("Enter transaction amount"))
                        flag = int(input("Press 1 for income Press 2 for expense"))
                        description = input("Enter description")
                        challanno = int(input("Enter challan no"))
                        trandate = input("Enter transaction date (dd-mm-yyyy)")
                        #convert string date into date
                        trandate = dt.strptime(trandate,"%d-%m-%Y")
                        values = [tourid,amount,flag,description,challanno,trandate]
                        mycursor.execute(sql,values)
                        print(mycursor.rowcount ," row inserted")
                        cn.database.commit()
                    except ValueError as e:
                        print("invalid date")
            elif transaction_choice==3:
                table = FetchTransactionId()
                if len(table)==0:
                    print("invalid transaction id")
                else:
                    try:
                        sql = "update transactions set amount=%s, flag=%s, description=%s, challanno=%s, trandate=%s where id=%s"
                        amount = int(input("Enter revised transaction amount"))
                        flag = int(input("Press 1 for income Press 2 for expense"))
                        description = input("Enter updated description")
                        challanno = int(input("Enter updated challan no"))
                        trandate = input("Enter updated transaction date (dd-mm-yyyy)")
                        #convert string date into date
                        trandate = dt.strptime(trandate,"%d-%m-%Y")
                        values = [amount,flag,description,challanno,trandate,transaction_id]
                        mycursor.execute(sql,values)
                        cn.database.commit()
                        print(mycursor.rowcount ," row updated")
                    except ValueError as e:
                        print("invalid date")
            elif transaction_choice==4:
                table = FetchTransactionId()
                if len(table) == 0:
                    print("invalid transaction id")
                else:
                    sql = "delete from transactions where id=%s"
                    values = [transaction_id]
                    mycursor.execute(sql,values)
                    cn.database.commit()
                    print("Transaction deleted")
            else:
                break
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
                DisplayTour()
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
                FetchTourId()
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
                FetchTourId()
                sql = "update trip set isdeleted=1 where id=%s"
                values = [tourid]
                mycursor.execute(sql,values)
                cn.database.commit()
                print(mycursor.rowcount, " trip deleted")
            else:
                print("good bye.") 
                break # loop break(stop)
            key = input("Press enter to continue")    
    elif choice==0:
        print("Good bye")
        break 