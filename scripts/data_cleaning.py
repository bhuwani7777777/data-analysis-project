import pandas as pd

# Load the dataset
df = pd.read_csv('../data/raw_data.csv')

# Check for missing values
print(df.isnull().sum())

# Drop rows with missing values
df_cleaned = df.dropna()

# Reset the index
df_cleaned.reset_index(drop=True, inplace=True)

# Save the cleaned dataset
df_cleaned.to_csv('../data/cleaned_data.csv', index=False)

print("Data cleaned successfully and saved as cleaned_data.csv")
