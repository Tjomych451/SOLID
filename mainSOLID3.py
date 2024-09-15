#################################################
#################################################
"""Task1"""


class SpeedCalculation:
    def calculate_allowed_speed(self, vehicle):  # S O L I
        if vehicle.get_type().lower() == "car":
            return vehicle.get_max_speed() * 0.8
        elif vehicle.get_type().lower() == "bus":
            return vehicle.get_max_speed() * 0.6
        return 0.0


class Vehicle:
    def __init__(self, max_speed: int, type: str):
        self.max_speed = max_speed
        self.type = type

    def get_max_speed(self):
        return self.max_speed

    def get_type(self):
        return self.type


#####################################################
##################################################### решение



class Vehicle:
    def __init__(self, max_speed):
        self.max_speed = max_speed


    def get_max_speed(self, speed):
        return self.max_speed

    def calculate_allowed_speed(self):
        pass

class Car:
    def calculate_allowed_speed(self):
        return self.get_max_speed()*0,8

class Bus:
    def calculate_allowed_speed(self):
        return self.get_max_speed()*0,6

class Motorbike:
    def calculate_allowed_speed(self):
        return self.get_max_speed()*1

class Speedcalculate:
    def calculate_allowed_speed(self, vehicle):
        return vehicle.calculate_allowed_speed()



#####################################################

"""Task2"""


class Employee:
    def __init__(self, name, dob, base_salary):
        self.name = name
        self.dob = dob
        self.base_salary = base_salary

    def get_emp_info(self):
        return f"name - {self.name} , dob - {self.dob}"

    def calculate_net_salary(self):
        tax = int(self.base_salary * 0.25)  # рассчитать налог другим способом
        return self.base_salary - tax


##################################################### решение


"""Task2"""


class Employee:
    def __init__(self, name, dob, base_salary):
        self.name = name
        self.dob = dob
        self.base_salary = base_salary

    def get_emp_info(self):
        return f"name - {self.name} , dob - {self.dob}"

    def get_base_salary(self):
        return self.base_salary



class calculate:
    def __init__(self, nalog = prozent/100):
        self.nalog = nalog

    def calculate_net_salary(self, employee :Employee ) -> float:
        base_salary = employee.get_base_salary
        tax = int(self.base_salary * self.nalog)  #
        return base_salary - tax




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
from abc import ABC, abstractmethod
import math


class ShapeVolume(ABC):
    # def __init__(self, shape):
    #     self.shape = shape

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def volume(self):
        pass

class Shape(ABC):
    @abstractmethod
    def area(self):
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

class Cube(ShapeVolume):
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

