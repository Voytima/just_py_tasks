# Triangle num:
n = int(input("Enter END num: "))


def triangle_nums(x, start=1):
    if start < x + 1:
        num_rec = start * (start + 1) / 2
        print(int(num_rec), end=' ')
        return triangle_nums(x, start+1)


triangle_nums(10)

print('\n')
for i in range(1, n + 1):
    num = i * (i + 1) / 2
    print(int(num), end=' ')
    i += i


# -----------------------
# 2) Decimal to binary:
# -----------------------
def to_binary(n):
    return int(f'{n:b}')


print(to_binary(2))
