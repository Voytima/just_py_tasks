# Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7] или [1, 7] или [1, 5, 6, 7] и т.д.
# Порядок элементов менять нельзя
from random import randint, shuffle


def get_sequence(n):
    uniq = []
    for i in range(len(n)):
        if n[i] == max(n[:i+1:]) and n[i] not in uniq:
            uniq.append(n[i])
    return uniq


if __name__ == '__main__':
    nums = int(input("How many numbers: "))
    num_list = [randint(1, 10) for i in range(nums)]
    shuffle(num_list)
    print(f"Init list: {[1, 5, 2, 3, 4, 6, 1, 7]}")
    print(f"Sequence list: {get_sequence([1, 5, 2, 3, 4, 6, 1, 7])}\n")
    print(f"Init list: {num_list}")
    print(f"Sequence list: {get_sequence(num_list)}\n")

