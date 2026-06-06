from vega_datasets import data 
import matplotlib.pyplot as plt 
import seaborn as sns 

# datasets = data.list_datasets() #return list of dataset 
# for item in datasets:
#     print(item)

#load dataset  as dataframe 
cars = data.cars()
print(cars)
sns.countplot(data=cars,x='Origin',hue='Cylinders')
plt.title("count plot chart")
plt.xlabel('Origin')
plt.ylabel('Count')
plt.show()
