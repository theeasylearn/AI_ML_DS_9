import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
# ============================================
# 1. Download Chicago crime data
# ============================================
url = (
    "https://data.cityofchicago.org/resource/"
    "ijzp-q8t2.csv"
    "?$limit=5000"
)
#load dataset 
df = pd.read_csv(url);
#display only 20 rows from dataset
# print(df.head(20))
#select input features 
X = df[[
    "latitude",
    "longitude",
]] 

#drop invalid date 
X = X.dropna()

#create model 
model = DBSCAN(eps=0.002,min_samples=10)
#model train
labels = model.fit_predict(X)
#adding new column Cluster 
X['cluster'] = labels
print(X.head(20))

print(X['cluster'].value_counts())
#create scatter plot chart
plt.figure(figsize=(10,12))

plt.scatter(X['latitude'],X['longitude'],c=X['cluster'])
plt.title("DBScan algorithm")
plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.show()
