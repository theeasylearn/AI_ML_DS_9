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

df = pd.read_csv(url)


# ============================================
# 2. Select latitude and longitude
# ============================================

df = df[
    [
        "latitude",
        "longitude"
    ]
]


# ============================================
# 3. Remove missing locations
# ============================================

df = df.dropna()


print("Number of crime records:")
print(len(df))


# ============================================
# 4. Prepare data for DBSCAN
# ============================================

X = df[
    [
        "latitude",
        "longitude"
    ]
]


# ============================================
# 5. Create DBSCAN model
# ============================================

model = DBSCAN(
    eps=0.002,
    min_samples=10
)


# ============================================
# 6. Perform clustering
# ============================================

labels = model.fit_predict(X)


# ============================================
# 7. Add cluster labels
# ============================================

df["Cluster"] = labels


# ============================================
# 8. Display results
# ============================================

print("\nClustered Crime Data:")
print(df.head(20))


# ============================================
# 9. Count clusters
# ============================================

print("\nCluster counts:")

print(
    df["Cluster"].value_counts()
)


# ============================================
# 10. Plot crime hotspots
# ============================================

plt.figure(figsize=(10, 7))


plt.scatter(
    df["longitude"],
    df["latitude"],
    c=df["Cluster"],
    s=10
)


plt.xlabel("Longitude")

plt.ylabel("Latitude")

plt.title(
    "Chicago Crime Hotspots using DBSCAN"
)

plt.grid(True)

plt.show()