def konwertuj_temperature(temperatura, z_skali, na_skale):
    if z_skali == "C" and na_skale == "F":
        return (temperatura * 9/5) + 32
    elif z_skali == "C" and na_skale == "K":
        return temperatura + 273.15
    elif z_skali == "F" and na_skale == "C":
        return (temperatura - 32) * 5/9
    elif z_skali == "F" and na_skale == "K":
        return (temperatura - 32) * 5/9 + 273.15
    elif z_skali == "K" and na_skale == "C":
        return temperatura - 273.15
    elif z_skali == "K" and na_skale == "F":
        return (temperatura - 273.15) * 9/5 + 32
    else:
        raise ValueError("Nieobsługiwana skala temperatury!")

# Przykładowe użyci
print(konwertuj_temperature(100, "C", "F")) 
print(konwertuj_temperature(0, "C", "K"))
