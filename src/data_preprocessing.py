import pandas as pd

# Load the dataset
file_path = "../data/starbucks_menu.csv"
data = pd.read_csv(file_path)

print("First 5 rows of the dataset:")
print(data.head())

print("\nDataset Info:")
print(data.info())

print("\nMissing values in each column:")
print(data.isnull().sum())

print("\nBasic statistics for numerical columns:")
print(data.describe())

# Fix column names: Strip leading/trailing spaces
data.columns = data.columns.str.strip()

print("Cleaned Column Names:")
print(data.columns)

# Handle missing value in 'Caffeine (mg)'
# Convert 'Caffeine (mg)' to numeric (forcing errors='coerce' will handle non-numeric data)
data['Caffeine (mg)'] = pd.to_numeric(data['Caffeine (mg)'], errors='coerce')

# Fill the missing value in 'Caffeine (mg)' with the column mean
data['Caffeine (mg)'] = data['Caffeine (mg)'].fillna(data['Caffeine (mg)'].mean())

# Convert 'Total Fat (g)' to numeric (handling non-numeric entries if any)
data['Total Fat (g)'] = pd.to_numeric(data['Total Fat (g)'], errors='coerce')

# Verify changes
print("\nMissing values after cleaning:")
print(data.isnull().sum())

print("\nUpdated Data Types:")
print(data.dtypes)

# Save cleaned data for future analysis
cleaned_file_path = "../data/cleaned_starbucks_menu.csv"
data.to_csv(cleaned_file_path, index=False)
print(f"\nCleaned data saved to: {cleaned_file_path}")
