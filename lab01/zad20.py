import math

a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Nieskończenie wiele miejsc zerowych")
        else:
            print("Nie ma miejsc zerowych")
    else:
        x0 = -c / b
        print("jedno miejjsce zerowe: x = {x0}")
else:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Dwa miejsca zerowe: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        x0 = -b / (2 * a)
        print(f"Jedno miejsce zerowe: x = {x0}")
    else:
        print("Nie ma miejsc zerowych")