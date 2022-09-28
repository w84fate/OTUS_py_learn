'''
Pipa M.A.
2022-09-28
'''

from homework_02.exceptions import LowFuelError, NotEnoughFuel, CargoOverload
from homework_02.base import Vehicle
from homework_02.engine import Engine
from homework_02.car import Car
from homework_02.plane import Plane

if __name__ == '__main__':
    print("Let's go")
    #testcases

    '''Проверка исключений'''
    # e = 3
    # if e == 1:
    #     raise LowFuelError
    # elif e == 2:
    #     raise NotEnoughFuel
    # elif e == 3:
    #     raise CargoOverload

    '''Проверка класса транспортного средства'''
    # v1 = Vehicle()
    # v1.start()
    # print(str(v1))
    # v2 = Vehicle(weight=50)
    # v2.start()
    # print(str(v2))
    # v3 =Vehicle(weight=50, fuel=5)
    # v3.start()
    # print(str(v3))
    # v4 = Vehicle(weight=50, fuel=5, fuel_consumption=2)
    # v4.start()
    # print(str(v4))
    # v4.move(100)
    # v5 = Vehicle(weight=50, fuel=0, fuel_consumption=2)
    # v5.start()
    # print(str(v5))

    v = Vehicle(fuel = 100, fuel_consumption=9)
    max_distance = v.fuel // v.fuel_consumption
    print(max_distance)
    distance = (1, max_distance)

    '''Проверка датакласса Двигатель и Автомобиль'''
    # eng = Engine(volume=3.6, pistons=6)
    # print(eng)
    #
    # c = Car()
    # print(c)
    # c.set_engine(engine=eng)
    # print(c.engine)

    '''Проверка самолета'''
    # p = Plane(max_cargo=1000.0)
    # print(p)
    # p.load_cargo(50)
    # print(p)
    # p.load_cargo(500)
    # print(p)
    #
    # print(p.remove_all_cargo())
    # print(p)

    # p2 = Plane(weight=50, fuel=0, fuel_consumption=2, max_cargo=1000.0)
    # print(p2)
