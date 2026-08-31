#import library 
import numpy as np 
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt 

#create input dataset 
spending = np.array([[10],[20],[30],[50],[100],[150],[200],[300]])

#create model
model = KMeans(n_clusters=4,random_state=42,n_init=1)

#train model 
model.fit(spending)

#get labels 
labels = model.labels_
print(labels)

#get centeroid
centeriods = model.cluster_centers_
print(centeriods)


customers = ['ram','shyam','shiv','vishnu','bramha','hanuman','Kuber','Indra']
#not required for model (optional)
# display output in below format
# Customer A spending 10 clusters 0 
for customer, category, spending_amount in zip(customers,labels,spending.flatten()):
    print(customer, category, spending_amount)

#create chart
plt.scatter(spending,labels)
plt.xlabel("Spending amount")
plt.ylabel("Score")
plt.title("Customer Segmentation ")
plt.show()

