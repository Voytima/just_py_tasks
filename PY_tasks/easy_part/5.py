# 5) Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

a = int(input("Enter integer num: "))

if a % 30 == int():
    print(f"Oops, num {a} shouldn't be a multiple of 30")
elif a % 5 == int() and a % 10 == int() or a % 15 == int():
    print(f"Number {a} is a multiple of 5 and 10 or 15 but not 30")
else:
    print("Another output")
