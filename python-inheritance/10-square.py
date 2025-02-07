#!/usr/bin/python3
# Classe Rectangle avec validation et méthode area
class Rectangle:
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

# Classe Square qui hérite de Rectangle
class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)  # Validation de la taille
        super().__init__(size, size)
        # On appelle le constructeur de Rectangleavec largeur et hauteur égales

    def area(self):
        return self.__width * self.__width  # Calcul de l'aire d'un carré

    def __str__(self):
        return f"[Square] {self.__width}/{self.__width}"

# Exemple d'utilisation
square = Square(5)
print(square)  # Output: [Square] 5/5
print("Area:", square.area())  # Output: Area: 25

