# Найти НОК двух чисел
from math import lcm


def get_lcm(a, b):
    return lcm(a, b)


if __name__ == '__main__':
    X = int(input("Enter first num: "))
    Y = int(input("Enter second num: "))
    print(f"Least common multiple for X and Y is {get_lcm(X, Y)}")
