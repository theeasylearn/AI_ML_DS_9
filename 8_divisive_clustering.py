# ============================================================
# DIVISIVE HIERARCHICAL CLUSTERING
# Example: Grouping 12 Countries
# ============================================================

# Step 1: Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


# ============================================================
# Step 2: Create the dataset
# ============================================================

data = {
    "Country": [
        "India",
        "China",
        "USA",
        "Germany",
        "Japan",
        "Brazil",
        "Canada",
        "Nigeria",
        "Switzerland",
        "Bangladesh",
        "Australia",
        "South Africa"
    ],

    # GDP per capita in USD
    "GDP_per_capita": [
        2700,
        13000,
        85000,
        55000,
        34000,
        11000,
        53000,
        1100,
        100000,
        2700,
        65000,
        6500
    ],

    # Life expectancy in years
    "Life_expectancy": [
        67,
        78,
        77,
        81,
        84,
        76,
        82,
        54,
        84,
        73,
        83,
        62
    ],

    # Internet users as percentage of population
    "Internet_usage": [
        55,
        76,
        97,
        92,
        87,
        81,
        94,
        36,
        96,
        45,
        97,
        75
    ]
}

#create dataframe
df = pd.DataFrame(data)
# print(df)

#select data for training 
x = df[[
    "GDP_per_capita",
    "Life_expectancy",
    "Internet_usage",
]]

#scale data 
scaler = StandardScaler()
x_scaled =  scaler.fit_transform(x)
# print(x_scaled)
def divisive_clustering(country,x_scaled,no_of_clusters):
    # print(countries,x_scaled,no_of_clusters)
    clusters = {
           0: list(range(len(countries))),
        }
    next_cluster_id = 1
    # print(clusters)
    while len(clusters)<no_of_clusters:
        #findout key with largest size list 
        max_cluster_id = max(clusters,key= lambda cluster_id : len(clusters[cluster_id]))
    
        #now get indexes 
        indexes = clusters[max_cluster_id]
        # print(indexes)
        #get data
        training_data = x_scaled[indexes]
        # print(training_data)
        model = KMeans(n_clusters=2,random_state=42,n_init=10)
        model.fit(training_data)
        labels = model.labels_
        list_1 = []
        list_2 = []
        for label,index in zip(labels,indexes):
            if label == 0:
                list_1.append(index)
            else:
                list_2.append(index)
        del clusters[max_cluster_id]
        clusters[next_cluster_id] = list_1
        next_cluster_id=next_cluster_id + 1 # 2
        clusters[next_cluster_id] = list_2
        next_cluster_id=next_cluster_id + 1
    return clusters
countries = df["Country"].tolist()
clusters = divisive_clustering(countries,x_scaled,4)
print(clusters)
for cluster in clusters.items():
    cluster_id = cluster[0]
    for index in cluster[1]:
        # print(index)
        df.loc[index,'clusters'] = cluster_id
print(df)
#we have clusters original dataframe 
