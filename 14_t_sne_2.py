import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
import kagglehub

# 1. Download the complete dataset folder using kagglehub
path = kagglehub.dataset_download("zalando-research/fashionmnist")
print("Dataset downloaded to:", path)

# 2. Read the CSV file directly with pandas
csv_file_path = os.path.join(path, "fashion-mnist_test.csv")
df = pd.read_csv(csv_file_path)

print("First 5 records:")
print(len(df))
y = df["label"].values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# print(X_scale)

tsne = TSNE(n_components=2,perplexity=30,random_state=42)
tsne_df = tsne.fit_transform(X_scaled)

print("t-SNE output shape:", tsne_df.shape)

plt.figure(figsize=(10, 7))
# Create a scatter plot
# c=y means points are colored according to their digit
scatter = plt.scatter(
    tsne_df[:, 0], #Take all rows and the first column of X_tsne.
    tsne_df[:, 1], #Take all rows and the second column of X_tsne.
    c=y, #Color each point according to which digit it represents.
    cmap="tab10", #tab10 provides a set of different colors suitable for categorical values such as:
    s=15 #s means size of each point.
)

# Add color bar to show digit numbers
plt.colorbar(scatter, label="Digit")

# Add title and labels
plt.title("t-SNE Visualization of Fashion MNIST Digits")
plt.xlabel("t-SNE Dimension 1")
plt.ylabel("t-SNE Dimension 2")

# Display the graph
plt.show()


