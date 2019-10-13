# рабочим каталогом должен быть тот-же каталог, в котором нахоядтся файлы cars.py и avtosalons.py
from cars import (
    Car,
    supercar,
)
from cars import Car as MyCar

# cars.init()
my_car = supercar

salon = Salon([])
car1 = Car('Mazda3', 'black', 10000)
car2 = MyCar('Mazda3', 'black', 10000)
# car1.color = 'black'

print(type(car1))
print(str(car1))
print(repr(car1))

print(car1==car2)