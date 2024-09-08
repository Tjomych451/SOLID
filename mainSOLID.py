#####################################################
"""Task3"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def volume(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        # ссылаемся на суперкласс
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 2 * math.pi * self.radius

    def volume(self):
        raise NotImplementedError("Circle does not have volume")


class Cube(Shape):
    def __init__(self, edge):
        self.edge = edge

    def area(self):
        return 6 * self.edge * self.edge

    def volume(self):
        return self.edge * self.edge * self.edge

##################################################### решение

class Shape(ABC):
    def __init__(self, shape):
        self.shape = shape

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def volume(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        # ссылаемся на суперкласс
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 2 * math.pi * self.radius

    def volume(self):
        raise NotImplementedError("Circle does not have volume")

class Cube(Shape):
    def __init__(self, edge):
        # ссылаемся на суперкласс
        super().__init__("Cube")
        self.edge = edge

    def area(self):
        return 6 * self.edge * self.edge

    def volume(self):
        return self.edge * self.edge * self.edge

#####################################################
from abc import ABC, abstractmethod

"""Task4"""


class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height

#####################################################


class Figure(ABC):
    # def __init__(self, figure_type):
    #     self.figure_type = figure_type

    @abstractmethod
    def calcul_area(self):
        pass

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calcul_area(self):
        return self.width * self.height

class Square(Figure):
    def __init__(self, width):
        self.width = width
        # self.height = width
    def calcul_area(self):
        return self.width ** 2

