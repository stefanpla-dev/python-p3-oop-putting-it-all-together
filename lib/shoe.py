#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size): #condition, cobble, repair not included here because they are independent of the initial creation of the shoe instance
        self.brand = brand
        self._size = size
        self.repaired = False #default repair status
        self.condition = "Used" #default condition

    def get_size(self):
        return self._size

    def set_size(self, new_size):
        if type(new_size) == int:
            self._size = new_size
        else:
            print("size must be an integer")

    size = property(get_size, set_size)

    def cobble(self):
        self.repaired = True
        self.condition = "New"
        print("Your shoe is as good as new!")
    
   
