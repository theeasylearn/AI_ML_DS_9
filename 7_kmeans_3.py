'''
The example represents a delivery company that wants to group 12 delivery areas according to:
    Distance from the city center 
    DailyOrders in that area 
The objective is to discover natural groups of areas without predefined labels.
That makes this an example of Unsupervised Learning → Clustering → K-Means
There are 12 areas:
There are 4 columns describing each area, but only two are actually used for clustering:
Distance + DailyOrders
Name|   zone|     distance| no of delivery
A	    North   	2	    95
B	    North   	3	    90
C	    North   	4	    100
D	    North   	5	    85
E	    East	    10	    55
F	    East	    11	    60
G	    East	    12	    50
H	    East	    13	    58
I	    South   	20  	20
J	    South   	21  	25
K	    South   	22  	18
L	    South   	23  	22

'''
#import library 
import pandas as pd 
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt 

#create dictionary
x = {
    'name': ['A','B','C','D','E','F','G','H','I','J','K','L'],
    'zone': ['North','North','North','North','East','East','East','East','South','South','South','South'],
    'distance' : [2,3,4,5,10,11,12,13,20,21,22,23],
    'delivery' : [95,90,100,85,55,60,50,58,20,25,18,22],
}
#create dataframe 
df = pd.DataFrame(x)
print(df)

training_df = df[
    ['distance','delivery']
]
print(training_df)

#scaling (put data in same range)
scaler = StandardScaler()
x_scaled = scaler.fit_transform(training_df)

#first decide k (no of clusters) using elbow method
inertia = []

for no_of_clusters in range(1,7):
    model = KMeans(n_clusters=no_of_clusters,random_state=42,n_init=1)
    model.fit(x_scaled)
    inertia.append(model.inertia_)
# print(inertia)
#create line chart
plt.figure(figsize=(6,8))
plt.plot(range(1,7),inertia)
plt.xlabel("no of clusters")
plt.ylabel("inertia")
plt.show()

#actually model train 
model = KMeans(n_clusters=3,random_state=42,n_init=1)
model.fit(x_scaled)

#add clusters into training_df 
df['cluster'] = model.labels_

print(df)


