class MyError(Exception):
    def __init__(self, errors):
        self.errors = errors

    def __str__(self):
        return f"dfsdfsdf: {self.errors}"

def divide(a, b):
    if b == 0:
        raise ValueError('Деление на 0 запрещено')
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError('Разрешено деление только целых чисел.')
    return a / b


def divide_list(data):
    """ Производит деление для каждой пары значений из итерируемого объекта data """
    result = []
    errors = []
    for a, b in data:
        try:
            result.append((a, b, divide(a, b)))
        except Exception as e:
            errors.append((a, b, str(e)))
    if errors:
        raise MyError(errors)
    return result

data = [
    (-1, 1),
    (1, -1),
    (0, 0),
#     (1, 0),
    (0, 1),
    (1, 1),
#     (0.1, 1)
]
try:
    for a, b, result in divide_list(data):
        print(f"{a} / {b} = {result}")
except MyError as e:
    for a, b, err_msg in e.errors:
        print(f"{a} / {b} = {err_msg}")