import connect as cn 
mycursor = cn.database.cursor()

sql = "delete from trip where id=%s"

id = int(input("Enter trip id to delete"))
values = [id]

mycursor.execute(sql,values)

cn.database.commit()
print(mycursor.rowcount, " trip deleted")