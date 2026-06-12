import matplotlib.pyplot as plt 
import seaborn as sns 
titanic = sns.load_dataset('titanic')
print(titanic)
sns.scatterplot(x='age',y='fare',data=titanic,hue='pclass',palette=['red','green','yellow'])
plt.grid(which='both')
plt.legend(title='pclass', labels=['first', 'second', 'third'])
plt.show()