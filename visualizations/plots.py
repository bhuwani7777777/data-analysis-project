import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('../data/cleaned_data.csv')

# Plot a bar chart
df['column_name'].value_counts().plot(kind='bar')
plt.title('Column Name Distribution')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()
