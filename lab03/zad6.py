def szukajWLiscie(lista, a):
    if isinstance(a, (int, float)):
        wartosc = a
    elif isinstance(a, str):
        if a.isdigit():
            wartosc = int(a)
        else:
            wartosc = sum(ord(znak) for znak in a)
    elif isinstance(a, bool):
        wartosc = int(a)
    else:
        raise TypeError("nieobslugiwany typ")

    liczba_wystapien = lista.count(a)
    print(f"Ilość wystąpien {a} wynosi {liczba_wystapien}")

lista_przykl = [1, 2, 3, 2, 5, 2, "42", True, False]
szukajWLiscie(lista_przykl, 2)
szukajWLiscie(lista_przykl, "42")
szukajWLiscie(lista_przykl, "abc")
szukajWLiscie(lista_przykl, True)
szukajWLiscie(lista_przykl, False)