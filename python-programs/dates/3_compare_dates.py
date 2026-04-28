from datetime import datetime as dt 

arrival_date = input("Enter Hotel arrival date (dd-mm-YYYY): ")

# convert string into date
arrival_date = dt.strptime(arrival_date, "%d-%m-%Y").date()

print("Your arrival date:", arrival_date)

current_date = dt.now().date()
print("Current date:", current_date)

if current_date < arrival_date:
    print("Your booking is eligible for 100% refund")
else:
    print("Your booking is not eligible for refund")