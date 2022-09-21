# 1) По двум заданным числам проверить является ли одно квадратом второго

# try:
#     a = int(input("Enter num a: "))
#     b = int(input("Enter num b: "))
#     if a*2 == b:
#         print("a is square of b")
#     elif b*2 == a:
#         print("b is square of a")
#     else:
#         print("a or b not a square of each other")
# except (TypeError, ValueError):
#     print("You have to enter nums")
"""------------------------------------------------------------------------"""
# 2) Найти максимальное из пяти чисел
# import random
#
# a = [random.randint(0, 100) for i in range(5)]
#
# print(a)
# find_max = max(a)
#
# print(f"The biggest num is: {find_max}")
"""------------------------------------------------------------------------"""
# 3) Вывести на экран числа от -N до N

# a = int(input(f"Enter the lowest value: "))
# b = int(input(f"Enter the highest value: "))
#
# for i in range(a, b):
#     print(i)
"""------------------------------------------------------------------------"""
# 4) Показать первую цифру дробной части числа
#
# a = float(input("Enter any num (int/float): "))
# b = int((a * 10) % 10)
#
# print(b)
"""------------------------------------------------------------------------"""
# 5) Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

# a = int(input("Enter integer num: "))
#
# if a % 30 == int():
#     print(f"Oops, num {a} shouldn't be a multiple of 30")
# elif a % 5 == int() and a % 10 == int() or a % 15 == int():
#     print(f"Number {a} is a multiple of 5 and 10 or 15 but not 30")
# else:
#     print("Another output")
"""------------------------------------------------------------------------"""
# 6) Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.
# import calendar
#
# date = int(input("Enter week day number 0-6: "))
# if date == 5 or date == 6:
#     print(f"Day: {date} - {calendar.day_name[date]} - weekend :)")
# else:
#     print(f"Day: {date} - {calendar.day_name[date]} - not a weekend :(")
"""------------------------------------------------------------------------"""
# 7) Сообщить в какой четверти координатной плоскости или на какой оси находится точка
# с координатами Х и У


# def coords(a, b):
#     if a == 0 and b == 0:
#         print("Point lies in zero point")
#     elif a > 0 and b > 0:
#         print("Point lies in first quarter")
#     elif a > 0 > b:
#         print("Point lies in fourth quarter")
#     elif a < 0 and b < 0:
#         print("Point lies in third quarter")
#     elif a < 0 < b:
#         print("Point lies in second quarter")
#     elif a == 0 and b > 0 or b < 0:
#         print("Point lies on y axis")
#     else:
#         print("Point lies on x axis")
#
#
# x = int(input("enter x: "))
# y = int(input("enter y: "))
# coords(x, y)

# 8) Найти расстояние между двумя точками пространства
import math

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

dist = math.sqrt(((x1 - x2) ** 2) + (y1 - y2) ** 2)
print(dist)
