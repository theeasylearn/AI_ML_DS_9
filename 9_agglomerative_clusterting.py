import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering

from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram

# ============================================
# 1. Create customer dataset
# ============================================

data = {
    "Customer": [
        "C1", "C2", "C3",
        "C4", "C5", "C6",
        "C7", "C8", "C9",
        "C10", "C11", "C12"
    ],

    "AnnualIncome": [
        15, 18, 20,
        45, 48, 50,
        80, 85, 90,
        30, 33, 35
    ],

    "Purchases": [
        3, 4, 5,
        10, 11, 12,
        20, 21, 22,
        7, 8, 8
    ]
}
# create dataframe
df = pd.DataFrame(data)
print(df)

#select input features
x = df[[
    "AnnualIncome",
    "Purchases",
]]

print(x)

#data scale
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)
print(x_scaled)

ward_linkage = linkage(x_scaled,method='ward')

#create dendogram 