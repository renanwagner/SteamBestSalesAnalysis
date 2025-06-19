import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from math import sqrt

# Configure Pandas display options to show all columns and full width
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Load the dataset
df = pd.read_csv('bestSelling_treated.csv')

# Display the first 30 registers
print(df.head(30))

# Display the correlation between two or more columns
print('Correlation between amount of reviews, reviews rate and downloads:\n',
      df[['all_reviews_number_k', 'reviews_like_rate', 'estimated_downloads_k']].corr())

corr_generation = df[['generation', 'year']].corr()
print('Correlation between console generation and year:\n', corr_generation)

corr_length = df[['length_MinMax', 'estimated_downloads_MinMax']].corr()
print(corr_length)

corr_rating_review = df[['rating_MinMax', 'reviews_like_rate_MinMax']].corr()
print(corr_rating_review)

corr_rating_downloads = df[['rating_MinMax', 'estimated_downloads_MinMax']].corr()
print(corr_rating_downloads)

corr_rating_revenue = df[['rating_MinMax', 'total_revenue_MinMax']].corr()
print(corr_rating_revenue)

corr_review_rating_revenue = df[['reviews_like_rate_MinMax', 'total_revenue_MinMax']].corr()
print(corr_review_rating_revenue)

corr_price_length = df[['price_MinMax', 'length_MinMax']].corr()
print(corr_price_length)

# Make previsions based on Linear Regression
