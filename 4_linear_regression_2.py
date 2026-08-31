'''
create an example of linear regression algorithm which predict a house's selling price based on its size (in square feet) and the number of bedrooms.
House,      Size (X1​ in sq ft),        Bedrooms (X2​),   Selling Price (Y in thousands $)
A,         "1,500",                     3,              300
B,         "1,800",                     4,              350
C,          "2,400",                    3,              450
D,          "3,000",                    5,              550
E,          800,                        1,              180
'''
#import library 
import numpy as np 
from sklearn.linear_model import LinearRegression

#create input dataset 
house = np.array([[1500,3],[1800,4],[2400,3],[3000,5],[800,1]])

#create output dataset
price = np.array([300,350,450,550,180])

#create model 
model = LinearRegression()

#modal train 
model.fit(house,price)

#predict house price 
vila = np.array([[5000,6]])

predicted_price = model.predict(vila)
print("vila's price prediction = ",predicted_price)


apartment = np.array([[2000,3]])

predicted_price = model.predict(apartment)
print("apartment's price prediction = ",predicted_price)