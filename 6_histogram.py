import matplotlib.pyplot as plt 
import seaborn as sns 

#load dataset 
titanic = sns.load_dataset('titanic')

sns.histplot(x='age',data=titanic,kde=False,bins=10)
plt.xlabel('Age')
plt.ylabel('count')
plt.title("Titanic dataset")
plt.show()