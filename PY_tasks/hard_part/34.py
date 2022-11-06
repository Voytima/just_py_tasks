# Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность и содержащие
# максимальное количество элементов. Порядок элементов менять нельзя
# Примеры: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#          [5, 2, 3, 4, 6, 1, 7]    => [2, 3, 4, 6, 7]
def max_sequence(n):
    if not n:
        return []

    max_s = [[] for i in range(len(n))]
    max_s[0].append(n[0])

    # старт со второго элемента в списке
    for i in range(1, len(n)):
        for j in range(i):  # сделать для каждого элемента в подсписке n[0…i-1]

            # найти самую длинную возрастающую подпоследовательность, которая заканчивается на n[j]
            # где n[j] меньше, чем текущий элемент n[i]
            if n[j] < n[i] and len(max_s[j]) > len(max_s[i]):
                max_s[i] = max_s[j].copy()

        # включает n[i] в max_s[i]
        max_s[i].append(n[i])

    # j будет хранить индекс max_s
    j = 0
    for i in range(len(n)):
        if len(max_s[j]) < len(max_s[i]):
            j = i

    print(max_s)
    return max_s[j]


if __name__ == '__main__':
    _list1 = [1, 5, 2, 3, 4, 6, 1, 7]
    # _list2 = [5, 2, 3, 4, 6, 1, 7]
    print(max_sequence(_list1))
    # print(max_sequence(_list2))
