import pandas as pd
import numpy as np

# Configure Pandas display options to show all columns and full width
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Load the dataset
df = pd.read_csv('bestSelling_games.csv')

# Display the first 30 rows of the dataset
print(df.head(30))

# Display the number of rows and columns of the dataset
print('Table Shape:\n', df.shape)

# Show the datatypes of each column
print('Data Types:\n', df.dtypes)

# Show the null values in each column
print('Amount of null values:\n', df.isnull().sum())

# Show descriptive statistics for each column (including non-numerical)
print('Descriptive Statistics:\n', df.describe(include='all'))

# Transform the release date column
df['release_date'] = pd.to_datetime(df['release_date'], format='%d %b, %Y')

# Create new columns for day, month and year
df['day'] = df['release_date'].dt.day
df['month'] = df['release_date'].dt.month
df['year'] = df['release_date'].dt.year

# Create a new column for total revenue
df['total_revenue'] = df['price'] * df['estimated_downloads']

# Treat the zero values replacing by 'Free to Play' and 'N/A'
df['price'] = df['price'].replace(0.00, 'Free to Play')
df['total_revenue'] = df['total_revenue'].replace(0.000000e+00, 'N/A')

# Classify the games by generation
conditions = [
    (df['release_date'] > pd.to_datetime('01/01/2020')),
    (df['release_date'] > pd.to_datetime('01/01/2011')),
    (df['release_date'] > pd.to_datetime('01/01/2004')),
    (df['release_date'] > pd.to_datetime('01/01/1998')),
    (df['release_date'] > pd.to_datetime('01/01/1994'))
]
# Define what values will appear on the column
choices = ['9', '8', '7', '6', '5']

# Create a new column to generation
df['generation'] = np.select(conditions, choices, default='Not Classified')

# Display the first 30 rows of the dataset
print(df.head(30))