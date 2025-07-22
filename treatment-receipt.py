import pandas as pd

# Configure Pandas display options to show all columns and full width
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Load the Dataset
df = pd.read_csv('bestSelling_treated.csv')

# Treat the zero values replacing by 'Free to Play' and 'N/A'
df['price'] = df['price'].replace(0.00, 'Free to Play')
df['total_revenue_million'] = df['total_revenue_million'].replace(0.000000e+00, 'N/A')

# Filter only the registers that has receipt
df_model = df[(df['total_revenue_million'] != 'N/A') & (df['price'] != 'Free to Play')]

# Display the first 30 rows of the Dataframe
print(df_model.head(30))

# Save the treatment file
df_model.to_csv('bestSelling_treated_receipt.csv', index=False)