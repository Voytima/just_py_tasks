# 8) Задать список из n чисел последовательности (1+1/n)**n и вывести на экран их сумму.
def sequence(num):
    _list = [(1 + 1 / i) ** i for i in range(1, num+1)]
    return f"sum: {round(sum(_list), 2)}"


if __name__ == '__main__':
    n = int(input("How many nums: "))
    print(sequence(n))
