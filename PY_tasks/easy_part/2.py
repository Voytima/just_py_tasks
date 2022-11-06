# Найти максимальное из пяти чисел
import random

a = [random.randint(0, 100) for i in range(5)]

print(a)
find_max = max(a)

print(f"The biggest num is: {find_max}")
