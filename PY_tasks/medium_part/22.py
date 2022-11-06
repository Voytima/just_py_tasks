# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]
def pair_mult(arr):
    return [arr[i] * arr[len(arr) - i - 1] for i in range(len(arr) // 2 + 1 if len(arr) % 2 else len(arr) // 2)]


if __name__ == '__main__':
    _list1 = [2, 3, 4, 5, 6]    # => [12, 15, 16]
    _list2 = [2, 3, 5, 6]   # => [12, 15]
    print(pair_mult(_list1))
    print(pair_mult(_list2))
