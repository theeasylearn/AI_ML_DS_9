import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
    roc_curve,
    roc_auc_score
)
import kagglehub 
# https://share.gemini.google/KpZrjtAsAwax
# ============================================================
# 1. download Dataset
# ============================================================
path = kagglehub.dataset_download("nikhil1e9/loan-default")

df = pd.read_csv(path + "/Loan_default.csv")
print("size of dataset ", df.shape)
print("column ", df.columns.tolist())
print(df.head(5))
# binary encoding
df['HasMortgage'] = df['HasMortgage'].map({'Yes': 1, 'No': 0})
df['HasDependents'] = df['HasDependents'].map({'Yes': 1, 'No': 0})
df['HasCoSigner'] = df['HasCoSigner'].map({'Yes': 1, 'No': 0})

#Nominal Fields (Use One-Hot Encoding)
df = pd.get_dummies(df, columns=['EmploymentType', 'MaritalStatus', 'LoanPurpose','Education'], drop_first=True)
print("After Encoding...")
print(df.head(5))
y = df['Default']
df = df.drop(columns=['LoanID','Default'])
print("Column Names ",df.columns.to_list())
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)
X_train, X_test, y_train, y_test = train_test_split(df,y,test_size=0.20,random_state=42)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)

y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test,y_pred)
cm = confusion_matrix(y_test,y_pred)
TN, FP, FN, TP = cm.ravel()
precision = precision_score(y_test,y_pred)
recall = recall_score(y_test,y_pred)
f1 = f1_score(y_test,y_pred)
specificity = TN / (TN + FP)
y_probability = knn.predict_proba(
    X_test
)[:, 0]

fpr, tpr, thresholds = roc_curve(
   y_test,y_pred
)
auc = roc_auc_score(
   y_test,y_pred
)
print(f"Accuracy    : {accuracy:.4f}")
print(f"Precision   : {precision:.4f}")
print(f"Recall      : {recall:.4f}")
print(f"F1 Score    : {f1:.4f}")
print(f"Specificity : {specificity:.4f}")
print(f"AUC         : {auc:.4f}")
print(cm)
print("\nConfusion Matrix Values:")
print("True Negative :", TN)
print("False Positive:", FP)
print("False Negative:", FN)
print("True Positive :", TP)
plt.figure(figsize=(8, 6))
plt.plot(
    fpr,
    tpr,
    label=f"KNN (AUC = {auc:.3f})"
)
plt.plot(
    [0, 1],
    [0, 1],
    linestyle="--",
    label="Random Classifier"
)
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.grid()
plt.show()