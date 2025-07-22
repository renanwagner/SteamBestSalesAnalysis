import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as mlb
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Configure Pandas display options to show all columns and full width
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

sns.set(style='whitegrid', palette='pastel')
plt.rcParams['figure.figsize'] = (12, 6)

# Load the dataset
df = pd.read_csv('bestSelling_treated_receipt.csv')

print(df.head(30))

sns.histplot(df['rating'], kde=True).set_title('Rating Distribuition')
plt.show()

sns.histplot(df['price'], kde=True).set_title('Price Distribution')
plt.show()

sns.histplot(df['estimated_downloads_k'], kde=True)
plt.title('Downloads Distribution')
plt.xlim(0, 20000)
plt.xticks(range(0, 20001, 1000))
plt.tight_layout()
plt.show()

sns.histplot(df['total_revenue_million'], kde=True)
plt.title('Receipt Distribution')
plt.xlim(0, 1000)
plt.xticks(range(0, 1001, 100))
plt.tight_layout()
plt.show()

sns.histplot(df['reviews_like_rate'], kde=True).set_title('Reviews Rating Distribution')
plt.show()

sns.histplot(df['length'], kde=True).set_title('Length Distribution')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x='year', data=df)
plt.xticks(rotation=45)
plt.title('Number of Games Released per Year')
plt.tight_layout()
plt.show()

sns.countplot(x='generation', data=df, order=sorted(df['generation'].unique()))
plt.title('Games per Console Generation')
plt.tight_layout()
plt.show()

corr_downloads = df[['all_reviews_number_k', 'reviews_like_rate', 'estimated_downloads_k']].corr()
sns.heatmap(corr_downloads, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation: Reviews Number, Reviews Rate and Downloads')
plt.tight_layout()
plt.show()

corr_generation = df[['generation', 'year']].corr()
sns.heatmap(corr_generation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation: Generation and Year')
plt.tight_layout()
plt.show()

corr_length = df[['length_MinMax', 'estimated_downloads_MinMax']].corr()
sns.heatmap(corr_length, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation: Length and Downloads')
plt.tight_layout()
plt.show()

corr_rating_review = df[['rating_MinMax', 'reviews_like_rate_MinMax']].corr()
sns.heatmap(corr_rating_review, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation: Critic Rating and Rating Review')
plt.tight_layout()
plt.show()

corr_rating_downloads = df[['rating_MinMax', 'estimated_downloads_MinMax']].corr()
sns.heatmap(corr_rating_downloads, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation: Critic Rating and Downloads')
plt.tight_layout()
plt.show()

corr_price_length = df[['price_MinMax', 'length_MinMax']].corr()
sns.heatmap(corr_price_length, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation: Price and Length')
plt.tight_layout()
plt.show()

tag_order = df.groupby('main_tag')['price'].median().sort_values().index
mlb.figure(figsize=(20, 10))
sns.boxplot(data=df, x='main_tag', y='price', order=tag_order)
mlb.xticks(rotation=90)
mlb.title('Price Distribution Per Genre')
mlb.tight_layout()
mlb.show()

generation_order = df.groupby('generation')['price'].median().sort_values().index
plt.figure(figsize=(20, 10))
sns.boxplot(data=df, x='generation', y='price', order=generation_order)
plt.title('Price Distribution Per Generation')
plt.tight_layout()
plt.show()

sns.violinplot(data=df, x='generation', y='rating')
plt.title("Critic's Rating per Generation")
plt.tight_layout()
plt.show()

sns.violinplot(data=df, x='generation', y='reviews_like_rate_MinMax')
plt.title("Critic's Rating per Generation")
plt.tight_layout()
plt.show()

plt.figure(figsize=(20, 10))
heatmap_tag = pd.crosstab(df['year'], df['main_tag'])
ordered_tag = heatmap_tag.sum(axis=0).sort_values(ascending=False)
sns.heatmap(heatmap_tag, cmap='magma', linewidths=0.3, linecolor='grey')
plt.title('Release Year per Genre', fontsize=18)
plt.xlabel('Genre', fontsize=14)
plt.ylabel('Year', fontsize=14)
plt.tight_layout()
plt.show()

plt.figure(figsize=(20, 10))
heatmap_feature = pd.crosstab(df['year'], df['main_feature'])
ordered_feature = heatmap_feature.sum(axis=0).sort_values(ascending=False)
sns.heatmap(heatmap_feature, cmap='viridis', linewidths=0.3, linecolor='grey')
plt.title('Release Year per Feature', fontsize=18)
plt.xlabel('Feature', fontsize=14)
plt.ylabel('Year', fontsize=14)
plt.tight_layout()
plt.show()

plt.figure(figsize=(20, 10))
heatmap_restriction = pd.crosstab(df['year'], df['age_restriction'])
ordered_restriction = heatmap_restriction.sum(axis=0).sort_values(ascending=False)
sns.heatmap(heatmap_restriction, cmap='viridis', linewidths=0.3, linecolor='grey')
plt.title('Release Year per Age Restriction', fontsize=18)
plt.xlabel('Age Restriction', fontsize=14)
plt.ylabel('Year', fontsize=14)
plt.tight_layout()
plt.show()

sns.scatterplot(data=df, x='price', y='estimated_downloads_k')
plt.title('Price vs Downloads')
plt.tight_layout()
plt.show()

sns.scatterplot(
    data=df,
    x='year',
    y='price',
    hue='age_restriction',
    size='reviews_like_rate',
    alpha=0.6,
    palette='tab10',
    edgecolor='black',
    linewidth=0.5
)
plt.title('Relation Between Year Release and Price (Coloring by Age Restriction and Sizing by Reviews Rate)')
plt.xlabel('Release Year')
plt.ylabel('Price')
plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Age Restriction and Rate')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

fig1 = px.scatter(
    df,
    x='year',
    y='price',
    size='estimated_downloads_k',
    color='main_tag',
    size_max=150,
    hover_name='game_name',
    title='Price vs Release Year (Color by Tag/Size by Receipt)'
)
fig1.update_layout(
    legend_title_text='Main Gender',
    template='plotly_white'
)
fig1.show()

grouped = df.groupby('main_tag')['total_revenue_million'].sum().sort_values()
fig2 = go.Figure(go.Bar(
    x=grouped.values,
    y=grouped.index,
    orientation='h',
    marker=dict(color='skyblue'),
    name='Total Receipt'
))
fig2.update_layout(
    title='Total Receipt per Gender',
    xaxis_title='Receipt',
    yaxis_title='Gender',
    template='ggplot2'
)
fig2.show()

fig3 = px.treemap(
    df,
    path=['main_tag', 'age_restriction'],
    values='total_revenue_million',
    title='Receipt Participation per Genre and Age Restriction',
    color='main_tag',
)
fig3.update_layout(margin=dict(t=50, l=25, r=25, b=25))
fig3.show()

top_genres = df.groupby('main_tag')['total_revenue_million'].sum().nlargest(10).index
df_filtered = df[df['main_tag'].isin(top_genres)]
fig4 = px.sunburst(
    df_filtered,
    path=['main_tag', 'main_feature', 'age_restriction'],
    values='total_revenue_million',
    title='Receipt Distribution (Genre > Feature > Restriction)',
    color='main_tag'
)
fig4.show()