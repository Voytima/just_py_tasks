# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.
def set_data(numbs):
    with open(numbs, 'w') as f:
        _list = f.write(sequence)
        return _list


def get_data(numbs):
    with open(numbs, 'r') as f:
        _list = f.read() + ' '
        _list = list(map(int, _list.split()))
        return _list


def find_num(numbs):
    for i in range(len(numbs) - 1):
        if numbs[i+1] - numbs[i] > 1:
            return numbs[i] + 1


def num_adder(numbs):
    for i in range(len(numbs) - 1):
        if numbs[i+1] - numbs[i] > 1:
            numbs.insert(i+1, numbs[i] + 1)
    return numbs


if __name__ == '__main__':
    sequence = input("Enter numbers via space: ")

    finder = 'Add_number_for_32.txt'
    nums_list = set_data(finder)
    nums = get_data(finder)

    print(get_data(finder))
    print(find_num(nums))
    print(num_adder(nums))
