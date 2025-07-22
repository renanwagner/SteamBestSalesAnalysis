import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from math import sqrt
from sklearn.linear_model import LinearRegression

# ConfigurSe Pandas display options to show all columns and full width
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Load the dataset
df = pd.read_csv('bestSelling_treated_receipt.csv')

# Display the first 30 registers
print(df.head(30))

# Show descriptive statistics for each column (including non-numerical)
print('Descriptive Statistics:\n', df.describe(include='all'))

# Display the correlation between two or more columns

corr_downloads = df[['all_reviews_number_k', 'reviews_like_rate', 'estimated_downloads_k']].corr()
print(f'Correlation between amount of reviews, reviews rate and downloads:\n {corr_downloads}')

corr_generation = df[['generation', 'year']].corr()
print(f'Correlation between console generation and year:\n {corr_generation}')

corr_length = df[['length_MinMax', 'estimated_downloads_MinMax']].corr()
print(f'Correlation between length and downloads:\n {corr_length}')

corr_rating_review = df[['rating_MinMax', 'reviews_like_rate_MinMax']].corr()
print(f'Correlation between critic rate and reviews rate:\n {corr_rating_review}')

corr_rating_downloads = df[['rating_MinMax', 'estimated_downloads_MinMax']].corr()
print(f'Correlation between critic rating and downloads:\n {corr_rating_downloads}')

corr_rating_revenue = df[['rating_MinMax', 'total_revenue_MinMax']].corr()
print(f'Correlation between console rating and receipt:\n {corr_rating_revenue}')

corr_price_length = df[['price_MinMax', 'length_MinMax']].corr()
print(f'Correlation between console price and length:\n {corr_price_length}')

# Make previsions based on Linear Regression
x_price = df[['price_MinMax', 'estimated_downloads_MinMax']].fillna(0)
y_revenue = df['total_revenue_MinMax'].replace('N/A', 0).astype(float)

x_price_train, x_price_test, y_revenue_train, y_revenue_test = train_test_split(x_price, y_revenue, test_size=0.2, random_state=42)

model_recept = LinearRegression()
model_recept.fit(x_price_train, y_revenue_train)

y_revenue_pred = model_recept.predict(x_price_test)

print('-------- Making recept previsions based on price and downloads --------')
print(f'R2 = {r2_score(y_revenue_test, y_revenue_pred):.2f}')
print(f'RMSE = {sqrt(mean_squared_error(y_revenue_test, y_revenue_pred)):.2f}')

x_reviews = df[['all_reviews_number_MinMax', 'rating_MinMax', 'reviews_like_rate_MinMax']].fillna(0)
y_downloads = df['estimated_downloads_MinMax'].replace('N/A', 0).astype(float)

x_reviews_train, x_reviews_test, y_downloads_train, y_downloads_test = train_test_split(x_reviews, y_downloads, test_size=0.2, random_state=42)

model_downloads = LinearRegression()
model_downloads.fit(x_reviews_train, y_downloads_train)

y_downloads_pred = model_downloads.predict(x_reviews_test)

print('\n -------- Making downloads previsions based on reviews -------- ')
print(f'R2 = {r2_score(y_downloads_test, y_downloads_pred):.2f}')
print(f'RMSE = {sqrt(mean_squared_error(y_downloads_test, y_downloads_pred)):.2f}')

x_like_rate = df[['rating_MinMax']].fillna(0)
y_rating = df['reviews_like_rate_MinMax'].replace('N/A', 0).astype(float)

x_like_rate_train, x_like_rate_test, y_rating_train, y_rating_test = train_test_split(x_like_rate, y_rating, test_size=0.2, random_state=42)

model_rating = LinearRegression()
model_rating.fit(x_like_rate_train, y_rating_train)

y_rating_pred = model_rating.predict(x_like_rate_test)

print('\n -------- Making reviews like rate previsions based on rating -------- ')
print(f'R2 = {r2_score(y_rating_test, y_rating_pred):.2f}')
print(f'RMSE = {sqrt(mean_squared_error(y_rating_test, y_rating_pred)):.2f}')

x_features = df[['year']].fillna(0)
y_price = df['generation'].replace('N/A', 0).astype(float)

x_features_train, x_features_test, y_price_train, y_price_test = train_test_split(x_features, y_price, test_size=0.2, random_state=42)

model_price = LinearRegression()
model_price.fit(x_features_train, y_price_train)

y_price_pred = model_price.predict(x_features_test)

print('\n -------- Making generation previsions based on the year of release -------- ')
print(f'R2 = {r2_score(y_price_test, y_price_pred):.2f}')
print(f'RMSE = {sqrt(mean_squared_error(y_price_test, y_price_pred)):.2f}')