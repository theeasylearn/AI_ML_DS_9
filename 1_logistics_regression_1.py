# /* Develop Logistic regression example that will predict 
# students will pass or fail based upon no of study hours  */
#import library 
import numpy as  np 
from sklearn.linear_model import LogisticRegression

#create dataset for input
hours = np.array([[1],[2],[3],[4],[5],[6],[7],[8]])
#create labels for input dataset 
result = np.array([0,0,0,1,1,1,1,1])

#create model
model = LogisticRegression()

#train model 
model.fit(hours,result)

#predict label for new input 
prediction = model.predict([[9]])
print("prediction of 9 hours study",prediction)
if prediction[0] == 1:
    print("student is passed")
else:
    print("student is failed")

#findout probability of fail or pass for the student who have studies 9 hour 
probability = model.predict_proba([[9]])
print("probability of fail or pass",probability)

#predict label for new input 
prediction = model.predict([[2.5]])
print("prediction of 2.5 hours study",prediction)

#findout probability of fail or pass for the student who have studies 9 hour 
probability = model.predict_proba([[2.5]])
print("probability of fail or pass in case 2.5 hour study",probability)

#display model accuracy 
score = model.score(hours,result)
print(score)



