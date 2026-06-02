import matplotlib.pyplot as plt 
import seaborn as sns 

tips = sns.load_dataset('tips')
# print(tips)
sns.boxplot(x='day',y='tip',data=tips)
plt.grid(which='both')
plt.show()