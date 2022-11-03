# 6) Подсчитать сумму цифр в вещественном числе.
def num_sum_counter(num):
    str_num = str(num)
    _sum = 0
    for i in str_num:
        if i == '.':
            _sum += 0
        else:
            _sum = _sum + int(i)
    return _sum


if __name__ == "__main__":
    n = input("Enter any num (dec or float): ")
    print(num_sum_counter(n))
