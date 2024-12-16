import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

file_path = "../output/pca_results.csv"
pca_data = pd.read_csv(file_path)

# ---- 1. Find the Optimal Number of Clusters (Elbow Method) ----
inertia = []  # List to store inertia values for each k
silhouette_scores = []

k_values = range(2, 8)  # Test for 2 to 7 clusters
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(pca_data)
    inertia.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(pca_data, kmeans.labels_))

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
optimal_k = 3  # Optimal k based on the elbow and silhouette plots
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
pca_data['Cluster'] = kmeans.fit_predict(pca_data)

# ---- 3. Visualize Clusters in 2D (First Two Principal Components) ----
plt.figure(figsize=(8, 6))
for cluster in range(optimal_k):
    plt.scatter(pca_data.loc[pca_data['Cluster'] == cluster, 'PC1'],
                pca_data.loc[pca_data['Cluster'] == cluster, 'PC2'],
                label=f'Cluster {cluster}')
plt.title("Clusters Visualized on Principal Components")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend()
plt.show()

# ---- 4. Save Clustered Data ----
pca_data.to_csv("../output/clustered_pca_results.csv", index=False)
print("Clustered PCA results saved to '../output/clustered_pca_results.csv'")

# ---- 5. Summarize Cluster Insights ----
# Load the original cleaned data
cleaned_data_path = "../data/cleaned_starbucks_menu.csv"
cleaned_data = pd.read_csv(cleaned_data_path)

# Merge Cluster Assignments with Original Data
clusters = pca_data['Cluster']
cleaned_data_with_clusters = cleaned_data.copy()
cleaned_data_with_clusters['Cluster'] = clusters

# Summarize Cluster Means (Numeric Only)
numeric_columns = cleaned_data_with_clusters.select_dtypes(include='number').columns
cluster_summary = cleaned_data_with_clusters.groupby('Cluster')[numeric_columns].mean()

# Display the Cluster Insights
print("Cluster Nutritional Summary:")
print(cluster_summary)

# Save the summary to a CSV file
output_path = "../output/cluster_summary.csv"
cluster_summary.to_csv(output_path)
print(f"Cluster summary saved to: {output_path}")


import matplotlib.pyplot as plt

# Load the cluster summary
cluster_summary = pd.read_csv("../output/cluster_summary.csv")

# Plot mean values for each cluster across selected features
features_to_plot = ['Calories', 'Total Fat (g)', 'Sugars (g)', 'Protein (g)']

for feature in features_to_plot:
    plt.figure(figsize=(8, 6))
    plt.bar(cluster_summary['Cluster'], cluster_summary[feature], color=['blue', 'orange', 'green'])
    plt.title(f'Mean {feature} by Cluster')
    plt.xlabel('Cluster')
    plt.ylabel(feature)
    plt.grid(axis='y')
    plt.show()
