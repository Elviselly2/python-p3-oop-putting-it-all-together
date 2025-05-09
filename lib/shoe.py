#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        if not isinstance(size, int):  # Ensure size is an integer
            print("size must be an integer")
            self._size = None
        else:
            self._size = size

        self.brand = brand  # Store the brand
        self.condition = "Used"  # Default condition

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"  # Set condition to "New" after repair

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    pass