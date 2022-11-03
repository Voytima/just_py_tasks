# 11) Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел
from time import time
print(time(), int(time()), int(time() % 1 * 100))

_list = []

x = 1
a = 2
b = 3
m = 100
c = 15

for i in range(c):
    x = (a * x + b) % m
    _list.append(x)

print(_list)
