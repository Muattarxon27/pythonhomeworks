import math

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

# Example usage
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print(v1)           # Output: Vector(1, 2, 3)
print(v1 + v2)     # Output: Vector(5, 7, 9)
print(v2 - v1)     # Output: Vector(3, 3, 3)
print(v1 * v2)     # Output: 32
print(3 * v1)      # Output: Vector(3, 6, 9)
print(v1.magnitude())  # Output: 3.7416573867739413
print(v1.normalize())  # Output: Vector(0.267, 0.534, 0.801)
