# 14) Найти сумму чисел списка стоящих на нечетной позиции
from random import randint


def odd_summ(_list):
    print(f'Array processing... {[_list[i] for i in range(len(_list)) if i % 2]}')
    return sum([_list[i] for i in range(len(_list)) if i % 2])


if __name__ == '__main__':
    print("\n***Odd indexes numbers calculations***")
    n = int(input("How many numbers:\n"))
    arr = [randint(0, 10) for x in range(n)]
    print(f"Array initialization... {arr}")
    print(f'Sum calcuations... {odd_summ(arr)}\n')
    print("Have a nice day! Bye...")
