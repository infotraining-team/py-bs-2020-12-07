import math as m

class Vector:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__length = None

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, val):    
        self.__length = None    
        self.__x = val

    def set_y(self, val):
        self.__length = None
        self.__y = val

    def __calculate_length(self):
        return m.sqrt(self.__x ** 2 + self.__y ** 2)

    def length(self):
        if self.__length == None:
            self.__length = self.__calculate_length()
        return self.__length