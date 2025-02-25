a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))

if a == 0:
    if b == 0:
        print("Funkcja ma nieskończenie wiele miejsc zerowych")
    else:
        print("Funkcja nie ma miejsc zerowych")

else:
    x0 = -b / a
    print("Miejsce zerowe funkcji: x = {x0}")