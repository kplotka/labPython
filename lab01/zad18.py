a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
c = int(input("Podaj trzecią liczbę: "))

if a > b:
    a, b = b, a
if b >c:
    b, c = c, b
if a > b:
    a, b = b, a

print("Liczby w kolejności od najmniejszej do największej: {a}, {b}, {c}")