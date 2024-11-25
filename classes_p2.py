# classes_p2.py

import math
from datetime import datetime

class Person:
    def __init__(self, first_name, last_name, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.base_salary = 50000
        self.bonus = 10  

    @property
    def birth_year(self):
        return self._birth_year

    @birth_year.setter
    def birth_year(self, year):
        current_year = datetime.now().year
        if not isinstance(year, int):
            raise TypeError("Birth year must be an integer.")
        if year <= 1900 or year > current_year:
            raise ValueError(f"Birth year must be between 1900 and {current_year}.")
        self._birth_year = year

    def set_birth_year(self, year):
        """Backwards-compatible method for setting birth year."""
        self.birth_year = year

    @property
    def age(self):
        current_year = datetime.now().year
        return current_year - self._birth_year

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, value):
        self.first_name, self.last_name = value.split(" ")

    @property
    def salary(self):
        return self.base_salary + (self.base_salary * self.bonus / 100)

class Circle:
    def __init__(self, radius):
        self._radius = None
        self._cached_area = None
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius must be a positive number.")
        self._radius = value
        self._cached_area = None

    @property
    def diameter(self):
        return 2 * self.radius

    @property
    def area(self):
        if self._cached_area is None:
            self._cached_area = math.pi * (self.radius ** 2)
        return self._cached_area

class Vehicle:
    vehicle_count = 0

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        Vehicle.vehicle_count += 1

    @classmethod
    def get_vehicle_count(cls):
        return cls.vehicle_count

    @staticmethod
    def classify_vehicle(vehicle_type):
        return f"This is a {vehicle_type}"


class ElectricVehicle(Vehicle):
    @staticmethod
    def classify_vehicle(vehicle_type):
        return f"This is an electric {vehicle_type}"


class DynamicClass:
    static_value = 0

    def __init__(self):
        self.attributes = {}

    def dynamic_attr(self, name, value):
        self.attributes[name] = value

    def __getattr__(self, name):
        if name in self.attributes:
            return self.attributes[name]
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")


class ValidatedAttribute:
    def __init__(self):
        self._value = 0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError("Value must be a positive integer.")
        self._value = new_value