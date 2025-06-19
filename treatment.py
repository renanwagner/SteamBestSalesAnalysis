import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Configure Pandas display options to show all columns and full width
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Load the dataset
df = pd.read_csv('bestSelling_games.csv')

# Display the first 30 rows of the dataset
print(df.head(30))

# Display the number of rows and columns of the dataset
print('Table Shape:\n', df.shape)

# Display the unique registers
uniques = df.nunique()
print(f'Unique Data Analysis:\n {uniques}')

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

# Create a new column for total revenue and transform that column to millions
df['total_revenue_million'] = df['price'] * df['estimated_downloads']
df['total_revenue_million'] = (df['total_revenue_million'] / 1e6).round(2)

# Transform the number of reviews and downloads to millions
df['all_reviews_number'] = (df['all_reviews_number'] / 1e3).round(2)
df['estimated_downloads'] = (df['estimated_downloads'] / 1e3).round(2)

# Rename the treated columns
df.rename(columns={
    'all_reviews_number': 'all_reviews_number_k',
    'estimated_downloads': 'estimated_downloads_k'
}, inplace=True)

# Extract the first tag and feature of each game
df['main_tag'] = df['user_defined_tags'].apply(lambda x: str(x).split(',')[0] if pd.notnull(x) else 'No Tag')
df['main_feature'] = df['other_features'].apply(lambda x: str(x).split(',')[0] if pd.notnull(x) else 'No Feature')

# Calculate MinMaxScaler
scaler = MinMaxScaler()
df['reviews_like_rate_MinMax'] = scaler.fit_transform(df[['reviews_like_rate']])
df['all_reviews_number_MinMax'] = scaler.fit_transform(df[['all_reviews_number_k']])
df['price_MinMax'] = scaler.fit_transform(df[['price']])
df['age_restriction_MinMax'] = scaler.fit_transform(df[['age_restriction']])
df['rating_MinMax'] = scaler.fit_transform(df[['rating']])
df['length_MinMax'] = scaler.fit_transform(df[['length']])
df['estimated_downloads_MinMax'] = scaler.fit_transform(df[['estimated_downloads_k']])
df['total_revenue_MinMax'] = scaler.fit_transform(df[['total_revenue_million']])

# Transform non-numerical columns to numerical format using LabelEncoder
le_developer = LabelEncoder()
le_tag = LabelEncoder()
le_feature = LabelEncoder()
le_supported = LabelEncoder()

df['developer_Cod'] = le_developer.fit_transform(df['developer'])
df['main_tag_Cod'] = le_tag.fit_transform(df['main_tag'])
df['main_feature_Cod'] = le_feature.fit_transform(df['main_feature'])
df['supported_os_Cod'] = le_feature.fit_transform((df['supported_os']))

# Treat the zero values replacing by 'Free to Play' and 'N/A'
df['price'] = df['price'].replace(0.00, 'Free to Play')
df['total_revenue_million'] = df['total_revenue_million'].replace(0.000000e+00, 'N/A')

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

# Save the treatment file
df.to_csv('bestSelling_treated.csv', index=False)
