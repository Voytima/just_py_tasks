# Сформировать список из  N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.
from random import randint


def list_creator():
    gen_lst = [randint(-100, 100) for x in range(n)]
    return gen_lst


if __name__ == "__main__":
    n = int(input('How many numbers: '))
    print(list_creator())
