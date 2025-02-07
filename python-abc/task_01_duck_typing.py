#!/usr/bin/python3
from abc import ABC, abstractmethod
import math

# Abstract class Shape
class Shape(ABC):
    # Abstract method for area
    @abstractmethod
    def area(self):
        pass

    # Abstract method for perimeter
    @abstractmethod
    def perimeter(self):
        pass


# Concrete class Circle inheriting from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Implementing the area method for Circle
    def area(self):
        return math.pi * self.radius ** 2

    # Implementing the perimeter method for Circle
    def perimeter(self):
        return 2 * math.pi * self.radius


# Concrete class Rectangle inheriting from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Implementing the area method for Rectangle
    def area(self):
        return self.width * self.height

    # Implementing the perimeter method for Rectangle
    def perimeter(self):
        return 2 * (self.width + self.height)


# Standalone function to print shape information
def shape_info(shape):
    # Print the area and perimeter of the shape (duck typing used here)
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


# Test the shape_info function with both Circle and Rectangle
circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=6)

print("Circle info:")
shape_info(circle)

print("\nRectangle info:")
shape_info(rectangle)
