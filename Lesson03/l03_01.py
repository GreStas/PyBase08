def input_float(msg):
    result = None
    while result is None:
        try:
            result = float(input('Введите ' + msg + ' :'))
        except ValueError:
            pass
    return result

x = input_float('делимое')
y = input_float('делитель')
try:
    print("Результат деления", x, 'на', y, 'равен', x / y)
except (ZeroDivisionError, ValueError):
    print('Будьте внимательнее! Делитель не может быть равен нулю.')
