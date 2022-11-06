# Показать первую цифру дробной части числа

a = float(input("Enter any num (int/float): "))
b = int((a * 10) % 10)

print(b)
