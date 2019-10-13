__all__ = ('Car', 'SportCar')

class Car(object):
    # __init__ = start

    def __init__(self, name, color, price):
        self.name = name
        if not isinstance(color, str):
            raise ValueError('color incorrect type')
        self.color = color

        if not isinstance(price, int):
            raise ValueError('price incorrect type')
        self.price = price

    def __str__(self):
        return f"{self.name} цвета {self.color} по цене {self.price}"

    def __repr__(self):
        # return f"Car({self.color}, {self.price})"
        return f"Car({repr(self.name)}, {repr(self.color)}, {repr(self.price)})"


class SportCar(Car):
    pass

def init():
    print('init')

supercar = Car('SuperCar', 'black', 1000000)


def len(obj):
    print('Oops!')