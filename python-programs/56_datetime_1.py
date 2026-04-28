#get current date & current time
from datetime import datetime as dt 
#dt is alias for datetime means we can use word dt instead of datetime 
date = dt.now()
week = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

today = week[date.weekday()] + " " + str(date.day) + "/" + str(date.month) + "/" + str(date.year)
print(today) #return current date

current = str(dt.now().hour) + ":" + str(dt.now().minute)
print(current) #return current time  