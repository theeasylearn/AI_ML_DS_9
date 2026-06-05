import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 

#load dataset 
result = pd.read_csv('marks_2.csv').squeeze()

sns.histplot(x='Mark',data=result,kde=False,bins=10)
plt.xlabel('Division')
plt.ylabel('Marks')
plt.title("Student result")
plt.show()