# Starbucks Nutritional Analysis

## Project Overview
This project analyzes the nutritional information of Starbucks beverages to identify meaningful patterns and groupings. Using **Principal Component Analysis (PCA)** for dimensionality reduction and **Hierarchical Cluster Analysis (HCA)**, beverages were segmented into distinct nutritional clusters. The project provides insights into calorie content, sugar levels, and other key nutritional metrics, offering practical value for health-conscious consumers and Starbucks menu optimization.

---

## Directory Structure

```plaintext
Starbucks_Nutritional_Analysis/
│
├── data/
│   ├── starbucks_menu.csv             # Original dataset from Kaggle
│   ├── cleaned_starbucks_menu.csv     # Preprocessed dataset
│
├── src/
│   ├── data_preprocessing.py          # Data cleaning and preparation
│   ├── eda_analysis.py                # Exploratory Data Analysis (EDA)
│   ├── pca_analysis.py                # Principal Component Analysis (PCA)
│   ├── hierarchical_clustering.py     # Clustering with HCA
│   ├── main.py                        # Workflow automation script
│
├── output/
│   ├── pca_results.csv                # PCA-transformed data
│   ├── hierarchical_clustered_results.csv # Data with cluster assignments
│   ├── hierarchical_cluster_summary.csv   # Nutritional summaries for each cluster
│
├── docs/
│   ├── Project_Report.docx            # Detailed project report
│
└── README.md                          # Project documentation (this file)
```

---

## How to Run the Project

### Prerequisites
Ensure you have the following installed:
- Python 3.8 or higher
- Required Python libraries:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn
  - scipy

### Running the Workflow
Execute the entire workflow using the `main.py` script:
```bash
python src/main.py
```

The outputs will be saved in the `output/` folder.

---

## Data Source
The dataset was sourced from Kaggle:
[Starbucks Menu Dataset](https://www.kaggle.com/datasets/henryshan/starbucks?resource=download)

- **Dataset Description**:
  - Includes nutritional information for Starbucks beverages.
  - Key features include:
    - `Beverage_category`, `Calories`, `Sugars (g)`, `Caffeine (mg)`, etc.

---

## Key Findings

### PCA
- Reduced data to 3 principal components explaining ~90% of the variance.
- Key drivers of variance include `Calories`, `Sugars (g)`, and `Total Fat (g)`.

### Clustering
- Hierarchical Cluster Analysis (HCA) identified 3 clusters:
  - **Cluster 1**: Low-calorie, low-sugar options (e.g., brewed teas).
  - **Cluster 2**: High-calorie and high-sugar beverages (e.g., Frappuccinos).
  - **Cluster 3**: Moderate-calorie, protein-rich beverages (e.g., lattes).

### Visualizations
- **Dendrograms**: Visualized clustering hierarchy and thresholds.
- **Bar Charts**: Compared mean nutritional values across clusters.

---

## Outputs
- **Cluster Summaries**: `output/hierarchical_cluster_summary.csv` contains average nutritional values for each cluster.
- **Visualizations**: Dendrograms and bar charts generated during analysis.

---

## Authors
- Andrici Sabina
- Ardelean Alexandru
- Boncu Ana Maria
- Anghelescu Adelina