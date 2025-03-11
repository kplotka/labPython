import statistics


def statystyki_listy(lista):
    mediana = statistics.median(lista)
    srednia = statistics.mean(lista)
    minimum = min(lista)
    maksimum = max(lista)
    odchylenie = statistics.stdev(lista) if len(lista) > 1 else 0

    return {
        "mediana": mediana,
        "średnia": srednia,
        "minimum": minimum,
        "maksimum": maksimum,
        "odchylenie_standardowe": odchylenie
    }

lista_liczb = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(statystyki_listy(lista_liczb))
