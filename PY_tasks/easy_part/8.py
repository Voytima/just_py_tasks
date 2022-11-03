# 8) Найти расстояние между двумя точками пространства
import math

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

dist = math.sqrt(((x1 - x2) ** 2) + (y1 - y2) ** 2)
print(dist)
