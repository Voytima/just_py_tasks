# Написать программу получающую набор произведений чисел от 1 до N.

# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]
def mult(n):
    result = []
    i = 1
    res = 1
    while i <= n:
        res = i * res
        result.append(res)
        i += 1
    return result


if __name__ == '__main__':
    num = int(input("Enter num: "))
    print(mult(num))
