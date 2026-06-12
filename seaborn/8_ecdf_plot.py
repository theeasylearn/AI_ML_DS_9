import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 

#load dataset 
covid = pd.read_csv('covid_death.csv').squeeze()

sns.ecdfplot(x='age',data=covid,color='red')
plt.xlabel('Age')
plt.title("covid 19 death")
plt.show()