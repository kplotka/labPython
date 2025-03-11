def szukajWLiscie(lista, a):
    liczba_wystapien = lista.count(a)
    print(f"Ilość wystąpien {a} wynosi {liczba_wystapien}")

lista_przykl = [1, 2, 3, 3, 2, 5, 1, 4, 2]
szukajWLiscie(lista_przykl, 2)