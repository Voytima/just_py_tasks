# По двум заданным числам проверить является ли одно квадратом второго

try:
    a = int(input("Enter num a: "))
    b = int(input("Enter num b: "))
    if a*2 == b:
        print("a is square of b")
    elif b*2 == a:
        print("b is square of a")
    else:
        print("a or b not a square of each other")
except (TypeError, ValueError):
    print("You have to enter nums")