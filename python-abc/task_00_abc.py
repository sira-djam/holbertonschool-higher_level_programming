#!/usr/bin/python
from abc import ABC, abstractmethod

class Animal(ABC):
    """
    An abstract class representing an animal.

    This class defines the common interface for all animals, ensuring that
    each subclass must implement the `sound` method.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by all subclasses to return the sound the animal makes.
        """
        pass


class Dog(Animal):
    """
    A class representing a dog, which is a subclass of Animal.

    Implements the `sound` method to return the sound a dog makes.
    """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    A class representing a cat, which is a subclass of Animal.

    Implements the `sound` method to return the sound a cat makes.
    """

    def sound(self):
        return "Meow"
