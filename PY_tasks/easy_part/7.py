# Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У
def coords(a, b):
    if a == 0 and b == 0:
        print("Point lies in zero point")
    elif a > 0 and b > 0:
        print("Point lies in first quarter")
    elif a > 0 > b:
        print("Point lies in fourth quarter")
    elif a < 0 and b < 0:
        print("Point lies in third quarter")
    elif a < 0 < b:
        print("Point lies in second quarter")
    elif a == 0 and b > 0 or b < 0:
        print("Point lies on y axis")
    else:
        print("Point lies on x axis")


x = int(input("enter x: "))
y = int(input("enter y: "))
coords(x, y)
