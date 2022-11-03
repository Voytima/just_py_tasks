# Вычислить число pi c заданной точностью d
# Пример: при d = 0.001, pi = 3.141. 10^(-1) <= d10 <= 10^(-10)
import time


def rounder(d):     # Формула Бэйли — Боруэйна — Плаффа
    return sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(d))


def rounder_big(d):     # Ряд Лейбница
    return 4 * (sum(1/x for x in range(1, d + 1, 4)) + sum(-1/x for x in range(3, d + 1, 4)))


if __name__ == '__main__':
    num = int(input("How many numbers after the decimal point: "))
    start = time.time()
    print(f"Формула Бэйли — Боруэйна — Плаффа\n{format(rounder(num), '.100')}")
    end = time.time()
    print(f"{round((end - start), 3)} seconds\n")
    start = time.time()
    print(f"Ряд Лейбница\n{format(rounder(num), '.100')}")
    end = time.time()
    print(f"{round((end - start), 3)} seconds")
