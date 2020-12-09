import math as m

class Vector:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__len = None

    def __set_x(self, val):    
        self.__len = None    
        self.__x = val

    def __set_y(self, val):
        self.__len = None
        self.__y = val

    def __calculate_length(self):
        return m.sqrt(self.__x ** 2 + self.__y ** 2)

    def __length(self):
        if self.__len == None:
            self.__len = self.__calculate_length()
        return self.__len

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y)
        return result

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __getitem__(self, i):
        if i == 0:
            return self.x
        elif i == 1:
            return self.y
        else:
            raise IndexError            

    def __setitem__(self, i, value):
        if i == 0:
            self.x = value
        elif i == 1:
            self.y = value
        else:
            raise IndexError

    def __repr__(self):
        return "Vector({}, {})".format(self.x, self.y)

    # def __str__(self):
    #     return "Vector at {}, {}".format(self.x, self.y)

    x = property(fset=__set_x, fget=lambda self : self.__x)
    y = property(fset=__set_y, fget=lambda self : self.__y)
    length = property(fget=__length)  # read-only property

v = Vector(1, 2)
print(v)
print(v.__repr__())

    