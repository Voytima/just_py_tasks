# В заданном списке вещественных чисел найдите разницу между max и min значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
def fraction_diff(arr):
    if not arr:
        return ValueError("Initial array cannot be empty!\nPlease, try again...")
    else:
        print(f"Initial array: {arr}")
        min_max = (list(map(lambda x: round(x % 1, 3) if x % 1 != 0 else min(arr) % 1, arr)))

        print(f'Max fraction value: {max(min_max)}')
        print(f'Min fraction value: {min(min_max)}')
        return f'Fraction max-min difference: {round(max(min_max) - min(min_max), 3)}\n'


if __name__ == '__main__':
    _list1 = [1.1, 1.2, 3.1, 5, 10.01]
    print(fraction_diff(_list1))
    """User input"""
    user_list = list(map(float, input("Enter float numbers via space:").split()))
    print(fraction_diff(user_list))
