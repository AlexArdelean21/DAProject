import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "../data/starbucks_menu.csv")

sns.set(style="whitegrid")
data = pd.read_csv(file_path)

# ---- 1. Distribution of Numerical Features ----
data.columns = data.columns.str.strip()
numeric_columns = data.select_dtypes(include=['number']).columns


# Plot histograms for each numerical column
# for col in numeric_columns:
#     plt.figure(figsize=(6, 4))
#     sns.histplot(data[col], bins=20, kde=True, color="blue")
#     plt.title(f'Distribution of {col}')
#     plt.xlabel(col)
#     plt.ylabel("Frequency")
#     plt.show()

# ---- 2. Correlation Heatmap ----
plt.figure(figsize=(10, 8))
correlation_matrix = data[numeric_columns].corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# ---- 3. Pair Plot for Highly Correlated Features ----
# Select top correlated features for visualization
top_features = ['Calories', 'Total Fat (g)', 'Sugars (g)', 'Protein (g)']
sns.pairplot(data[top_features])
plt.show()

# ---- 4. Boxplots for Outlier Detection ----
# for col in numeric_columns:
#     plt.figure(figsize=(6, 4))
#     sns.boxplot(y=data[col])
#     plt.title(f'Boxplot of {col}')
#     plt.ylabel(col)
#     plt.show()
