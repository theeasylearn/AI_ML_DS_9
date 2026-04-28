import mysql.connector as con 
try:
    database = con.connect(host='localhost',user='root',passwd='',database='ai_ml_ds_9',port='3306')
    print('database connected ....')
except con.Error as e:
    print("error in connection ")
    print(e.errno)
    print(e.msg)
