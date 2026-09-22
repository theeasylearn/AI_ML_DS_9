# ============================================================
# PCA - PATIENT HEALTH ANALYSIS
# ============================================================
# Step 1: Import libraries
from statistics import variance

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
df = None
def pca_process():
    global df 
    data = {
        "Patient": [
            "P01", "P02", "P03", "P04",
            "P05", "P06", "P07", "P08",
            "P09", "P10", "P11", "P12"
        ],
        "Age": [
            25, 32, 41, 48,
            55, 62, 29, 38,
            45, 52, 67, 72
        ],
        "Systolic_BP": [
            112, 118, 125, 132,
            140, 148, 115, 122,
            128, 136, 155, 162
        ],
        "Diastolic_BP": [
            72, 76, 80, 85,
            90, 94, 74, 78,
            82, 87, 98, 102
        ],
        "Cholesterol": [
            165, 175, 190, 205,
            220, 235, 170, 185,
            200, 215, 245, 255
        ],
        "Glucose": [
            88, 92, 98, 108,
            118, 128, 90, 96,
            105, 112, 135, 145
        ],

        "BMI": [
            21.5, 23.1, 25.4, 27.8,
            29.5, 31.2, 22.4, 24.8,
            26.9, 28.7, 33.0, 34.5
        ],

        "Heart_Rate": [
            68, 70, 74, 78,
            82, 85, 69, 72,
            76, 80, 88, 91
        ],

        "Activity": [
            60, 55, 45, 35,
            25, 20, 65, 50,
            40, 30, 15, 10
        ]
    }
    # Convert dictionary into DataFrame
    df = pd.DataFrame(data)
    print(df)
    #select input features
    X = df[
        [
            "Age",
            "Systolic_BP",
            "Diastolic_BP",
            "Cholesterol",
            "Glucose",
            "BMI",
            "Heart_Rate",
            "Activity",
        ]
    ]
    print(X)
    #scaling 
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(X)
    print(x_scaled)
    #CREATE PCA OBJECT
    model = PCA(n_components=2)
    pca_df = model.fit_transform(x_scaled)

    #convert it into dataframe
    pca_df = pd.DataFrame(pca_df,columns=['PC-1','PC-2'])
    print(pca_df)
    #display variance 
    variance_1 = model.explained_variance_ratio_[0]
    variance_2 = model.explained_variance_ratio_[1]
    print("PC-1 ",variance_1)
    print("PC-2 ",variance_2)
    print("Total variance ratio ",variance_1+variance_2)
    return pca_df #return dataframe that has principal components 

pca_df = pca_process()

#Create Model 
model = KMeans(n_clusters=3,random_state=42,n_init=10)

#model train 
model.fit(pca_df)
clusters = model.labels_
df['cluster'] = clusters
print(df)

