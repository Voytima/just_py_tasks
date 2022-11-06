# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
def uniq_values(nums):
    uniq = []
    repeatable = []

    for i in range(len(nums)):
        if nums[i] not in uniq:
            uniq.append(nums[i])
        else:
            uniq.remove(nums[i])
            repeatable.append(nums[i])

        for j in uniq:
            if j in repeatable and j in uniq:
                uniq.remove(j)

    return uniq


if __name__ == '__main__':
    numbers = [1, 2, 3, 5, 1, 5, 3, 10]
    n = list(input("Enter any numbers: "))
    print(n)
    print(uniq_values(n))
    print(uniq_values(numbers))
