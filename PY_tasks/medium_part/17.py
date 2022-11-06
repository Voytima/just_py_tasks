# Реализовать алгоритм перемешивания списка.
import random


def shuffle(nums):
    _list = [i for i in range(nums + 1)]
    random.shuffle(_list)
    return _list


if __name__ == '__main__':
    n = int(input("How many nums for list: "))
    print(shuffle(n))
