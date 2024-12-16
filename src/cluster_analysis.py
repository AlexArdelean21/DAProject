import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import os

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "../data/cleaned_starbucks_menu.csv")
data = pd.read_csv(file_path)

# Ensure numeric-only data is used for clustering
data_numeric = data.select_dtypes(include=['number'])
data_numeric = data_numeric.fillna(data_numeric.mean())

# ---- 1. Find the Optimal Number of Clusters (Elbow Method) ----
inertia = []
silhouette_scores = []

k_values = range(2, 8)
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(data_numeric)
    inertia.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(data_numeric, kmeans.labels_))

# Plot the Elbow Method
plt.figure(figsize=(8, 5))
plt.plot(k_values, inertia, marker='o', linestyle='--')
plt.title("Elbow Method for Optimal k")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.grid()
plt.show()

# Plot the Silhouette Scores
plt.figure(figsize=(8, 5))
plt.plot(k_values, silhouette_scores, marker='o', linestyle='--', color='orange')
plt.title("Silhouette Scores for Optimal k")
plt.xlabel("Number of Clusters")
plt.ylabel("Silhouette Score")
plt.grid()
plt.show()

# ---- 2. Perform K-Means with Optimal k ----
optimal_k = 3  # Based on Elbow/Silhouette plots
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
data['Cluster'] = kmeans.fit_predict(data_numeric)

output_path = os.path.join(current_dir, "../output/clustered_pca_results.csv")
data.to_csv(output_path, index=False)
print(f"Clustered data saved to: {output_path}")

# ---- 3. Summarize Cluster Means ----
numeric_columns = data.select_dtypes(include=['number']).columns
cluster_summary = data.groupby('Cluster')[numeric_columns].mean()

ssummary_path = os.path.join(current_dir, "../output/cluster_summary.csv")
cluster_summary.to_csv(summary_path)
print(f"Cluster summary saved to: {summary_path}")
