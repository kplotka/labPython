def sortuj_liste(lista, kierunek="rosnąco"):
    return sorted(lista, reverse=(kierunek == "malejąco"))

lista_liczb = [5, 3, 8, 1, 4]
print(sortuj_liste(lista_liczb))
print(sortuj_liste(lista_liczb, "malejąco"))
