# Составить список простых множителей натурального числа N


def primfacs(n):
    i = 2
    primfac = []
    if n == 1:
        primfac.append(n)
        return primfac
    else:
        while i * i <= n:
            while n % i == 0:
                primfac.append(i)
                n = n / i
            i = i + 1
        if n > 1:
            primfac.append(n)
        return primfac


if __name__ == '__main__':
    num = int(input("Enter natural num: "))
    print(primfacs(num))
