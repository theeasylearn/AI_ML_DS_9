import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 

election = pd.read_csv('election.csv')

sns.countplot(data=election,x='party',hue='state')
plt.title("Indian election result 2024")
plt.xlabel('Party')
plt.ylabel('Count')
plt.show()
