import copy

a = [list(range(5)), 5, 6, {1:2, 3:{4:[1,2,{5:6,7:8}]}}]
b = a.copy()
print(id(a[0]), id(b[0]))
b = copy.deepcopy(a)
print(id(a[0]), id(b[0]))
