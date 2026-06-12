import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
from vega_datasets import data 

#load car dataset 
cars = data.cars()
print(cars)
sns.stripplot(data=cars,x='Cylinders',y='Miles_per_Gallon',hue='Origin')
plt.xlabel('Cylinders')
plt.ylabel('Miles per Gallon')
plt.title("Car Milage Cyliender wise ")
plt.show()