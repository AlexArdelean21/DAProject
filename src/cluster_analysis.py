import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import matplotlib.pyplot as plt
import os

# Set file paths
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "../data/cleaned_starbucks_menu.csv")
output_dendrogram_path = os.path.join(current_dir, "../output/hierarchical_dendrogram.png")
output_clustered_data_path = os.path.join(current_dir, "../output/hierarchical_clustered_results.csv")

# Load the dataset
data = pd.read_csv(file_path)

# Ensure numeric-only data is used for clustering
data_numeric = data.select_dtypes(include=['number'])

# Standardize the dataset if necessary
# Optionally: from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# data_numeric = scaler.fit_transform(data_numeric)

# ---- 1. Perform Hierarchical Clustering ----
linkage_matrix = linkage(data_numeric, method='ward')  # Ward's method minimizes variance within clusters

# Plot the dendrogram
plt.figure(figsize=(10, 7))
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Sample Index")
plt.ylabel("Distance")
dendrogram(linkage_matrix, leaf_rotation=90., leaf_font_size=0., color_threshold=0.7 * max(linkage_matrix[:, 2]))
plt.axhline(y=150, color='r', linestyle='--')  # Example threshold for cutting the tree
plt.savefig(output_dendrogram_path)
plt.show()
print(f"Dendrogram saved to: {output_dendrogram_path}")

# ---- 2. Assign Cluster Labels ----
# Define a threshold distance to form clusters
threshold_distance = 150  # Modify as needed based on dendrogram
clusters = fcluster(linkage_matrix, t=threshold_distance, criterion='distance')

# Add cluster labels to the original data
data['Cluster'] = clusters

# Save the clustered dataset
data.to_csv(output_clustered_data_path, index=False)
print(f"Clustered data saved to: {output_clustered_data_path}")

# ---- 3. Summarize Cluster Means ----
numeric_columns = data.select_dtypes(include=['number']).columns
cluster_summary = data.groupby('Cluster')[numeric_columns].mean()

summary_path = os.path.join(current_dir, "../output/hierarchical_cluster_summary.csv")
cluster_summary.to_csv(summary_path)
print(f"Cluster summary saved to: {summary_path}")
