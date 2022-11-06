# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]
from random import randint


def unrepeatable_list(nums):
    # Var_1
    # return list(set(nums))

    # var_2
    unr_list = []
    for i in nums:
        if i not in unr_list:
            unr_list.append(i)
    return sorted(unr_list)


if __name__ == '__main__':
    n = int(input("How many nums in initial list: "))
    list_init = [randint(1, 10) for i in range(n)]
    print(list_init)
    print(unrepeatable_list(list_init))
