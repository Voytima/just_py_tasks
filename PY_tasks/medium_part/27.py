# Найти корни квадратного уравнения Ax² + Bx + C = 0.
# a) Математикой;
# b) Используя дополнительные библиотеки*
import math


def square_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    print(f"Discriminant is: {discriminant:.2f}")

    if discriminant < 0:
        return "No roots..."
    elif discriminant > 0:

        # a) mathematical
        x1 = (-b + discriminant ** 0.5) / (a * 2)
        x2 = (-b - discriminant ** 0.5) / (a * 2)

        # b) math library
        # x1 = (-b + math.sqrt(discriminant)) / (a * 2)
        # x2 = (-b - math.sqrt(discriminant)) / (a * 2)

        return f"Two roots: {x1:.2f} and {x2:.2f}"
    else:
        x = -b / (2 * a)
        return f"One root: {x:.2f}"


if __name__ == '__main__':
    n1 = float(input("Enter a: "))
    n2 = float(input("Enter b: "))
    n3 = float(input("Enter c: "))
    print(square_roots(n1, n2, n3))
