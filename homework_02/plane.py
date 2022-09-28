"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

class Plane(Vehicle):
    cargo: float = 0.0
    max_cargo: float

    # def __init__(self, weight:float, fuel:float, fuel_consumption:float,  max_cargo:float):
    #     self.max_cargo = max_cargo
    #     self.weight = weight
    #     self.fuel = fuel
    #     self.fuel_consumption = fuel_consumption

    def __init__(self, weight:float, fuel:float , fuel_consumption:float, max_cargo:float):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo


    def load_cargo(self, new_cargo):
        if self.cargo + new_cargo > self.max_cargo:
            raise CargoOverload
        else:
            self.cargo+=new_cargo

    def remove_all_cargo(self):
        prev_cargo = self.cargo
        self.cargo = 0.0
        return prev_cargo

    def __str__(self):
        return f'{self.__class__.__name__} status: weight={self.weight}; started={self.started}' \
               f'; fuel={self.fuel}; fuel_consumption={self.fuel_consumption}; max_cargo={self.max_cargo}; current cargo={self.cargo};'