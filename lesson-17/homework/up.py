import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
from mpl_toolkits.mplot3d import Axes3D

class Vector:
    def __init__(self, *components):
        self.components = tuple(components)

    def __repr__(self):
        return f"Vector{self.components}"

    def __add__(self, other):
        if not isinstance(other, Vector) or len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for addition.")
        return Vector(*[a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other):
        if not isinstance(other, Vector) or len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for subtraction.")
        return Vector(*[a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*[a * other for a in self.components])
        elif isinstance(other, Vector) and len(self.components) == len(other.components):
            return sum(a * b for a, b in zip(self.components, other.components))
        else:
            raise ValueError("Multiplication must be either scalar or dot product with another vector of the same dimension.")
    
    def __rmul__(self, other):
        return self * other

    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(*[a / mag for a in self.components])

# Database Reading
conn = sqlite3.connect('chinook.db')
df_customers = pd.read_sql_query("SELECT * FROM customers", conn)
print(df_customers.head(10))

# Inner Join: Customers & Invoices
df_invoices = pd.read_sql_query("SELECT * FROM invoices", conn)
df_customer_invoices = pd.merge(df_customers, df_invoices, on='CustomerId', how='inner')
total_invoices_per_customer = df_customer_invoices.groupby('CustomerId').size()
print(total_invoices_per_customer)
conn.close()

# JSON Reading
df_iris = pd.read_json('iris.json')
df_iris.columns = df_iris.columns.str.lower()
df_iris_selected = df_iris[['sepal_length', 'sepal_width']]
print(df_iris_selected.head())

# Calculate statistics for iris dataset
print("Iris dataset statistics:")
print(df_iris.describe().loc[['mean', '50%', 'std']])

# Excel Reading
df_titanic = pd.read_excel('titanic.xlsx')
df_titanic_filtered = df_titanic[df_titanic['Age'] > 30]
print(df_titanic_filtered.head())
print(df_titanic['Sex'].value_counts())

# Titanic age statistics
print("Titanic Age Stats:")
print("Min Age:", df_titanic['Age'].min())
print("Max Age:", df_titanic['Age'].max())
print("Total Age Sum:", df_titanic['Age'].sum())

# Parquet File Reading
df_flights = pd.read_parquet('flights.parquet')
print(df_flights[['origin', 'dest', 'carrier']].head())
print("Number of unique destinations:", df_flights['dest'].nunique())

# Check and fill missing values
df_flights.fillna(df_flights.mean(), inplace=True)
print("Missing values after filling:")
print(df_flights.isnull().sum())

# CSV File Reading
df_movies = pd.read_csv('movie.csv')
df_movies_filtered = df_movies[df_movies['duration'] > 120]
df_movies_sorted = df_movies_filtered.sort_values(by='director_facebook_likes', ascending=False)
print(df_movies_sorted.head())

# Movie dataset analysis
most_liked_director = df_movies.groupby('director_name')['director_facebook_likes'].sum().idxmax()
print("Director with highest total Facebook likes:", most_liked_director)

# Longest movies and their directors
print("Top 5 longest movies:")
print(df_movies.nlargest(5, 'duration')[['title', 'director_name']])

# Outer Join on Movie Data
df_movies_subset1 = df_movies[['director_name', 'color']]
df_movies_subset2 = df_movies[['director_name', 'num_critic_for_reviews']]

# Left Join
left_join_result = pd.merge(df_movies_subset1, df_movies_subset2, on='director_name', how='left')
print("Left Join Result Rows:", len(left_join_result))

# Full Outer Join (using outer join)
outer_join_result = pd.merge(df_movies_subset1, df_movies_subset2, on='director_name', how='outer')
print("Full Outer Join Result Rows:", len(outer_join_result))
