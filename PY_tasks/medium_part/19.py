# Определить, присутствует ли в заданном списке строк, некоторое число
def word_finder(num, _list):
    return f"Found your num {num} in list {str_lst}!" if {any(ch == num for ch in _list)} else "Nothing was found"


if __name__ == '__main__':
    _len = int(input("How many strings: "))
    str_lst = [input(f"Enter {i+1} string:\n") for i in range(_len)]
    number = input("Enter a num for checking: ")
    print(word_finder(number, str_lst))
