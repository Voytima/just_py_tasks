# Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях.

# Позиции хранятся в файле file.txt в одной строке одно число
import random


def file_writer(N):
    with open('file.txt', 'w', encoding='utf8') as file:
        for i in range(N):
            file.write(f"{random.randrange(0, 2*N)}\n")


def file_reader():
    with open('file.txt', 'r', encoding='utf8') as file:
        idx = list(map(int, file.readlines()))
    return idx


def calcs(N):
    list_nums = [i for i in range(-N, N + 1)]
    print(f"List of numbers: {list_nums}")
    file_writer(N)
    list_idx = file_reader()
    print(f"List of indexes: {list_idx}")
    mult = 1
    for i in range(len(list_idx)):
        mult *= list_nums[list_idx[i]]
    return mult


if __name__ == '__main__':
    nums = int(input("How many nums: "))
    print(calcs(nums))
