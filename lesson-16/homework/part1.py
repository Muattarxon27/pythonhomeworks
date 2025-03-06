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
print("Shape:", df_iris.shape)
print("Columns:", df_iris.columns)

# Excel Reading
df_titanic = pd.read_excel('titanic.xlsx')
print(df_titanic.head())

# Parquet File Reading
df_flights = pd.read_parquet('flights.parquet')
df_flights.info()

# CSV File Reading
df_movies = pd.read_csv('movie.csv')
print(df_movies.sample(10))

# Plotting f(x) = x^2 - 4x + 4
x = np.linspace(-10, 10, 100)
y = x**2 - 4*x + 4
plt.figure()
plt.plot(x, y, label='f(x) = x^2 - 4x + 4')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Quadratic Function Plot')
plt.legend()
plt.grid()
plt.show()

# Sine and Cosine Plot
x = np.linspace(0, 2 * np.pi, 100)
plt.figure()
plt.plot(x, np.sin(x), label='sin(x)', linestyle='--', color='r')
plt.plot(x, np.cos(x), label='cos(x)', linestyle='-', color='b')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine and Cosine Functions')
plt.legend()
plt.grid()
plt.show()

# 2x2 Subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
x = np.linspace(-2, 2, 100)
axs[0, 0].plot(x, x**3, 'g')
axs[0, 0].set_title('f(x) = x^3')
axs[0, 1].plot(x, np.sin(x), 'b')
axs[0, 1].set_title('f(x) = sin(x)')
x = np.linspace(0, 2, 100)
axs[1, 0].plot(x, np.exp(x), 'r')
axs[1, 0].set_title('f(x) = e^x')
axs[1, 1].plot(x, np.log(x+1), 'm')
axs[1, 1].set_title('f(x) = log(x+1)')
plt.tight_layout()
plt.show()

# Scatter Plot
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)
plt.figure()
plt.scatter(x, y, c='blue', marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot of Random Points')
plt.grid()
plt.show()

# Histogram
data = np.random.normal(0, 1, 1000)
plt.figure()
plt.hist(data, bins=30, alpha=0.75, color='green')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Normal Distribution')
plt.grid()
plt.show()

# 3D Surface Plot
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.cos(X**2 + Y**2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(x,y)')
ax.set_title('3D Surface Plot')
plt.show()

# Bar Chart
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]
plt.figure()
plt.bar(products, sales, color=['blue', 'green', 'red', 'purple', 'orange'])
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Sales Data')
plt.show()

# Stacked Bar Chart
time_periods = ['T1', 'T2', 'T3', 'T4']
category_A = [3, 5, 2, 8]
category_B = [4, 2, 6, 5]
category_C = [5, 3, 4, 6]
plt.figure()
plt.bar(time_periods, category_A, label='Category A')
plt.bar(time_periods, category_B, bottom=category_A, label='Category B')
plt.bar(time_periods, category_C, bottom=np.array(category_A) + np.array(category_B), label='Category C')
plt.xlabel('Time Periods')
plt.ylabel('Values')
plt.title('Stacked Bar Chart')
plt.legend()
plt.show()