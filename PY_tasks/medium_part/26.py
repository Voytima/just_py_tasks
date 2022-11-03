# 19) Строка содержит набор чисел. Показать большее и меньшее число. Символ-разделитель - пробел
def converter(nums):
    string = list(map(int, nums.split()))
    return f"Max: {max(string)}\nMin: {min(string)}"


if __name__ == '__main__':
    n = input("Enter nums via space: ")
    print(n)
    print(converter(n))
