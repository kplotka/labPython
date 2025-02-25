liczba = int(input("Podaj liczba: "))

jednosci = liczba % 10
dziesiatki = (liczba // 10) % 10
setki = (liczba // 100) % 10

print("Cyfra jedności: {jednosci}")
print("Liczba dziesiątek: {dziesiatki}")
print(f"Liczba setek: {setki}")