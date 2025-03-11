class Person:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def przedstaw_sie(self):
        return f"Mam na imię {self.imie} i mam {self.wiek} lat."

osoba = Person("Alicja", 25)
print(osoba.przedstaw_sie()) 
