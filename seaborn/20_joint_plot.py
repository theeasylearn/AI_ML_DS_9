import matplotlib.pyplot as plt 
import seaborn as sns 
from vega_datasets import data 

#load car dataset 
cars = data.cars()
print(cars)
sns.jointplot(data=cars,x='Cylinders',y='Miles_per_Gallon')
plt.xlabel('Cylinders')
plt.ylabel('Miles per Gallon')
plt.title("Cyliender wise Car Milage")
plt.show()