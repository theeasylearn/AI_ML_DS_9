from datetime import datetime as dt 
print(dt.now()) #return date and time 
print(dt.now().date()) #date
print(dt.now().time()) #time 
#display current time in 12 hours format 
hours = dt.now().hour #return hours of time 
minutes = dt.now().minute # return minutes of time 
ampm = ' am'
if hours>12:
    hours = hours - 12 
    ampm = ' pm'
print(hours,":",minutes,ampm)
