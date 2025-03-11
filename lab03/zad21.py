import random

def kamien_papier_nozyce():
    opcje = ["kamień", "papier", "nożyce"]
    komputer = random.choice(opcje)
    gracz = input("Wybierz (kamień, papier, nożyce): ").lower()

    if gracz not in opcje:
        print("Niepoprawny wybór!")
        return

    print(f"Komputer wybrał: {komputer}")

    if gracz == komputer:
        print("Remis!")
    elif (gracz == "kamień" and komputer == "nożyce") or \
         (gracz == "papier" and komputer == "kamień") or \
         (gracz == "nożyce" and komputer == "papier"):
        print("Wygrałeś!")
    else:
        print("Przegrałeś!")

kamien_papier_nozyce()
