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
conn.close()

# JSON Reading
df_iris = pd.read_json('iris.json')
df_iris.columns = df_iris.columns.str.lower()
df_iris_selected = df_iris[['sepal_length', 'sepal_width']]
print(df_iris_selected.head())

# Excel Reading
df_titanic = pd.read_excel('titanic.xlsx')
df_titanic_filtered = df_titanic[df_titanic['Age'] > 30]
print(df_titanic_filtered.head())
print(df_titanic['Sex'].value_counts())

# Parquet File Reading
df_flights = pd.read_parquet('flights.parquet')
print(df_flights[['origin', 'dest', 'carrier']].head())
print("Number of unique destinations:", df_flights['dest'].nunique())

# CSV File Reading
df_movies = pd.read_csv('movie.csv')
df_movies_filtered = df_movies[df_movies['duration'] > 120]
df_movies_sorted = df_movies_filtered.sort_values(by='director_facebook_likes', ascending=False)
print(df_movies_sorted.head())
