from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):
    weight = 500.0
    started = False
    fuel = 40.0
    fuel_consumption = 7.0

    def __init__(self, weight:float = weight, fuel:float = fuel, fuel_consumption:float = fuel_consumption):
        self.weight = float(weight)
        self.fuel = float(fuel)
        self.fuel_consumption = float(fuel_consumption)

    def start(self):
        if self.started == False:
            if self.fuel>0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, dist: float):
        if dist * self.fuel_consumption / 100 > self.fuel:
            raise NotEnoughFuel
        else:
            print('Remaining fuel: {}'.format(round(self.fuel - dist * self.fuel_consumption / 100, 3)))

    def __str__(self):
        return f'{self.__class__.__name__} status: weight={self.weight}; started={self.started}' \
               f'; fuel={self.fuel}; fuel_consumption={self.fuel_consumption};'