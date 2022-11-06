# Написать программу преобразования десятичного числа в двоичное
def decimal_to_binary(num):
    binary = ""
    while num:
        binary = str(num % 2) + binary
        num //= 2
    return binary


if __name__ == '__main__':
    n = int(input("Enter a num to convert: "))
    print(f'Decimal {n} --> {decimal_to_binary(n)} Binary')
