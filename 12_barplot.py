from vega_datasets import data 
import matplotlib.pyplot as plt 
import seaborn as sns 

# datasets = data.list_datasets() #return list of dataset 
# for item in datasets:
#     print(item)

#load dataset  as dataframe 
cars = data.cars()
print(cars)
sns.barplot(data=cars,x='Cylinders',y='Miles_per_Gallon',hue='Origin')
plt.title("bar plot chart")
plt.xlabel('Cylinders')
plt.ylabel('Miles_per_Gallon')
plt.show()
