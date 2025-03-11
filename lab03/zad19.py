def rysuj_i_policz_pole(ksztalt, wymiar):
    if ksztalt == "kwadrat":
        for _ in range(wymiar):
            print("* " * wymiar)
        return wymiar ** 2
    elif ksztalt == "koło":
        import math
        return math.pi * (wymiar ** 2)
    else:
        raise ValueError("Nieznana figura!")

print("Pole kwadratu:", rysuj_i_policz_pole("kwadrat", 4))
print("Pole koła:", rysuj_i_policz_pole("koło", 3))
