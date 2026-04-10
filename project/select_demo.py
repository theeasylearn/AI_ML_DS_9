import connect as cn 
#create cursor 
mycursor = cn.database.cursor(dictionary=True)

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
    
