#!/usr/bin/python3
# Parent class Fish
class Fish:
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")

# Parent class Bird
class Bird:
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")

# FlyingFish class that inherits from both Fish and Bird
class FlyingFish(Fish, Bird):
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")

# Instantiate a FlyingFish object
flying_fish = FlyingFish()

# Call the fly, swim, and habitat methods
flying_fish.fly()        # Output: The flying fish is soaring!
flying_fish.swim()       # Output: The flying fish is swimming!
flying_fish.habitat()    # Output: The flying fish lives both in water and the sky!

# Explore the Method Resolution Order (MRO)
print(FlyingFish.mro())   # Output: MRO list for FlyingFish
