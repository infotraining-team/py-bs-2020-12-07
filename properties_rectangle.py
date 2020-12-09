class Rectangle:
    def __init__(self, size):
        self.__size = size

    def __get_size(self):
        return self.__size

    def __set_size(self, size):
        self.__size = size

    def __get_area(self):
        return self.__size[0] * self.__size[1]

    area = property(fget=__get_area)
    size = property(fset=__set_size, fget=__get_size)

r = Rectangle((2, 3))
#print(r.get_area())
print(r.area)
#r.area = 100
print(r.size)
r.size = 4, 5
print(r.area)
