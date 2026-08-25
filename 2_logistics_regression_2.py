# /* Develop Logistic regression example that will predict whether a patient has Diabetes ($y=1$) or Does Not Have Diabetes ($y=0$) based on two input features: BMI ($x_1$) and Age in years ($x_2$). */
#import library 
import numpy as  np 
from sklearn.linear_model import LogisticRegression

#create dataset for input
# X contains the 2 input features: [BMI (x1), Age (x2)]
person_info = np.array([
    [22.5, 25],
    [31.0, 45],
    [24.0, 30],
    [35.5, 50],
    [27.2, 38],
    [33.1, 60]
])
# y contains the target labels: Diabetes Status (0 = No, 1 = Yes)
labels = np.array([0, 1, 0, 1, 0, 1])

#create model
model = LogisticRegression()

#train model
model.fit(person_info,labels)

#prediction 
rahul = np.array([[30.1,45]])
mona =  np.array([[31.2,50]])
ankit =  np.array([[28.5,41]])

print("prediction for rahul",model.predict(rahul))
print("prediction for mona",model.predict(mona))
print("prediction for ankit",model.predict(ankit))

print(model.score(person_info,labels))



