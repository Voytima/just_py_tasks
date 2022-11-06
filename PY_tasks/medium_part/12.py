# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
s1 = 'qwtdfghqwd234qwbncb'
s2 = 'qw'
index = s1.find(s2)


def counter(x, y):
    count = 0
    idx = 0
    while len(x) != 0:
        idx = x.find(y, idx)
        if idx != -1:
            count += 1
            idx += len(y)
        else:
            break
    return count


print(counter(s1, s2))
