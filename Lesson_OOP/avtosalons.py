# рабочим каталогом должен быть тот-же каталог, в котором нахоится файл cars.py
from cars import Car

__all__ = ('Salon',)

class Salon:

    def __init__(self, catalog):
        self.catalog = catalog
        self.cash = 0.0

    def append(self, name, color, price):
        from cars import supercar
        self.catalog.append(Car(name, color, price))

    def sail(self, name, color, price):
        car = None
        for i, obj in enumerate(self.catalog):
        # for obj in enumerate(self.catalog):
            if (obj.name, obj.color, obj.price) == (name, color, price):
                # i = self.catalog.index(obj)
                car = self.catalog.pop(i)
                self.cash += car.price
                return car
        else:
            raise ValueError('Автомобиль не найден')

# print(__name__)  # отладочный код для демонстрации значения переменной __all__ во время импорта или выполнения

if __name__ == '__main__':
    salon = Salon([])
    car1 = Car('Mazda3', 'black', 10000)
    car2 = Car('Mazda3', 'black', 10000)
    # car1.color = 'black'

    print(type(car1))
    print(str(car1))
    print(repr(car1))

    print(car1==car2)