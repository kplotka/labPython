a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
c = int(input("Podaj trzecią liczbę: "))

najwieksza = a

if b > najwieksza:
    najwieksza = b
if c > najwieksza:
    najwieksza = c

print("Największa liczba to: {najwieksza}")