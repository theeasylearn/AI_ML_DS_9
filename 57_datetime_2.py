from datetime import datetime as dt 
birthdate = "29/12/2022" #indian format 
print(birthdate)

#convert birthdate into actual date (string to date)
date1 = dt.strptime(birthdate,"%d/%m/%Y")
#by default strptime function convert string date into date in %Y-%m-%d
print(date1) #2022-12-29 00:00:00

#now display this date in us format 
print(dt.strftime(date1,"%m/%d/%Y")) #12/29/2022
