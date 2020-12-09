import math as m

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
          
    def length(self):
        return m.sqrt(self.x ** 2 + self.y ** 2)