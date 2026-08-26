#import library 
import numpy as np 
from sklearn.linear_model import LinearRegression

#create input dataset 
hours = np.array([[1],[2],[3],[4],[5],[6]])

#create output dataset
marks = np.array([30,40,50,60,65,70])

#create model 
model = LinearRegression()

#modal train 
model.fit(hours,marks)

#predict marks 
mansi = np.array([[7]])

predicted_marks = model.predict(mansi)
print("mansi's marks predicition = ",predicted_marks)

ronit = np.array([[5.5]])
predicted_marks = model.predict(ronit)
print("ronit's marks predicition = ",predicted_marks)
