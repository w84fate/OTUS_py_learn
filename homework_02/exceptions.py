"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
    def __init__(self): # real signature unknown
        self.message = 'Low fuel, need to refuel'

    def __str__(self):
        return self.message

class NotEnoughFuel(Exception):
    def __init__(self): # real signature unknown
        self.message = 'Not enough fuel, the car will stall out on the way and you will be eaten by wolves'

    def __str__(self):
        return self.message

class CargoOverload(Exception):
    def __init__(self): # real signature unknown
        self.message = 'Cargo cannot be loaded'

    def __str__(self):
        return self.message