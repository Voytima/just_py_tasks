# 4) Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


def _dict(num):
    gen_dict = {x: (x * 3 + 1) for x in range(1, num + 1)}
    return gen_dict


if __name__ == '__main__':
    n = int(input('How many numbers: '))
    print(_dict(n))
