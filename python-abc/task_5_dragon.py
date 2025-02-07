#!/usr/bin/python3
# Mixin for swimming abilities
class SwimMixin:
    def swim(self):
        print("The creature swims!")

# Mixin for flying abilities
class FlyMixin:
    def fly(self):
        print("The creature flies!")

# Dragon class that inherits from both SwimMixin and FlyMixin
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")

# Instantiate a Dragon object named draco
draco = Dragon()

# Demonstrate draco's abilities
draco.swim()  # Output: The creature swims!
draco.fly()   # Output: The creature flies!
draco.roar()  # Output: The dragon roars!
