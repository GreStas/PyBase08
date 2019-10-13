import pickle

data = (1.0, 'абракадабра abracadabra', 1, (1,2,3))

# Сериализуем объект data в байтовую строку b
b = pickle.dumps(data)
print(type(b), repr(b))

# Пишем b в файл
# ...
# Читаем b из файла
# ...

# Восстанавливаем объект в obj c помощью десериализации
obj = pickle.loads(b)
print(repr(obj))