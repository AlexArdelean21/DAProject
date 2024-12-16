import pandas as pd

# Load the dataset
file_path = "../data/starbucks_menu.csv"  # Path to the original dataset
data = pd.read_csv(file_path)

# ---- 1. Clean Column Names ----
data.columns = data.columns.str.strip()  # Strip leading/trailing spaces from column names

# ---- 2. Retain Necessary Columns ----
columns_to_keep = [
    'Beverage_category',   # Keep this column for cluster interpretation
    'Calories', 'Total Fat (g)', 'Trans Fat (g)', 'Saturated Fat (g)',
    'Sodium (mg)', 'Total Carbohydrates (g)', 'Cholesterol (mg)',
    'Sugars (g)', 'Protein (g)', 'Caffeine (mg)'
]
data = data[columns_to_keep]

# ---- 3. Convert Columns to Numeric ----
# Exclude 'Beverage_category' and convert all other columns to numeric
for col in data.columns:
    if col != 'Beverage_category':
        data[col] = pd.to_numeric(data[col], errors='coerce')  # Coerce invalid entries to NaN

# ---- 4. Handle Missing Values ----
# Separate numerical columns for processing
data_numeric = data.drop(columns=['Beverage_category'])

# Fill missing values in numerical columns with their column means
data_numeric = data_numeric.fillna(data_numeric.mean())

# Combine 'Beverage_category' back with processed numerical data
data_cleaned = pd.concat([data[['Beverage_category']], data_numeric], axis=1)

# ---- 5. Save the Cleaned Dataset ----
output_path = "../data/cleaned_starbucks_menu.csv"
data_cleaned.to_csv(output_path, index=False)

print(f"Cleaned data saved to: {output_path}")
