import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV data
df = pd.read_csv('data/sales_data.csv')

# Convert dates to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extract month and year
df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.year

# Group and summarize sales
monthly_sales = df.groupby(['Year', 'Month'])['Sales'].sum().reset_index()

# Plot
plt.figure(figsize=(12, 6))
sns.lineplot(x='Month', y='Sales', hue='Year', data=monthly_sales, marker='o')
plt.title('Monthly Sales Over Time')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid(True)
plt.tight_layout()
plt.show()
