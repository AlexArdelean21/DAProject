import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import os

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "../data/starbucks_menu.csv")

data = pd.read_csv(file_path)

# ---- 1. Check for Remaining NaNs ----
print("Checking for NaN values in numerical data before PCA:")
print(data.isnull().sum())

# Select only the numerical columns
data.columns = data.columns.str.strip()
data_numeric = data.select_dtypes(include=['number'])


# Double-check and handle missing values
data_numeric = data.select_dtypes(include=['number'])

# ---- 2. Standardize the Data ----
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data_numeric)

# ---- 3. Perform PCA ----
pca = PCA()
pca_data = pca.fit_transform(scaled_data)

# Explained variance ratio
explained_variance = pca.explained_variance_ratio_

# ---- 4. Visualize Explained Variance ----
plt.figure(figsize=(8, 5))
plt.plot(range(1, len(explained_variance) + 1), explained_variance.cumsum(), marker='o', linestyle='--')
plt.title("Explained Variance by Principal Components")
plt.xlabel("Number of Principal Components")
plt.ylabel("Cumulative Explained Variance")
plt.grid()
plt.show()

# ---- 5. Save PCA Results ----
pca_columns = [f"PC{i+1}" for i in range(len(explained_variance))]
pca_df = pd.DataFrame(pca_data, columns=pca_columns)

# Save PCA-transformed data
pca_df.to_csv("../output/pca_results.csv", index=False)
print("PCA results saved to '../output/pca_results.csv'")
