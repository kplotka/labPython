# Nonogram – gra logiczna w Pythonie

**Nonogram** to klasyczna gra logiczna zaimplementowana w języku Python z użyciem biblioteki `pygame`. Celem gry jest odkrycie ukrytego wzoru na planszy, wypełniając odpowiednie pola zgodnie ze wskazówkami liczbowymi dla wierszy i kolumn.

---

## Opis projektu

Projekt umożliwia graczowi:
- wybór poziomu trudności spośród dostępnych plansz,
- wypełnianie kratek oraz oznaczanie pól jako puste (znakiem „X”),
- zapisanie stanu gry oraz jego późniejsze wczytanie,
- sprawdzenie poprawności rozwiązania,
- kontynuowanie gry dzięki systemowi zapisów,
- grę w trybie okienkowym z obsługą zamykania aplikacji,
- dynamiczne dopasowanie planszy do rozmiaru poziomu i okna.

---

## Wymagania systemowe

- Python 3.9 lub nowszy
- Pygame w wersji 2.6.1

Instalacja zależności:
```bash
pip install pygame
```

## Struktura katalogów

```
Projekt/
├── levels/                  # Pliki poziomów w formacie JSON
├── screens/                 # Ekrany gry (menu, gra, zapisy, wybór poziomu)
│   ├── menu.py
│   ├── game.py
│   ├── dialogs.py
│   ├── level_select.py
│   ├── save_level_select.py
│   ├── save_list.py
├── grid.py                  # Logika planszy i rysowanie
├── main.py                  # Główna pętla aplikacji
├── puzzle.py                # Wczytywanie poziomów z plików JSON
├── utils.py                 # Operacje na zapisach gry
├── save.json                # Dane zapisanych gier
├── README.md                # Dokumentacja
```

## Uruchomienie gry

Aby uruchomić grę, należy wykonać plik 'main.py':
```bash
python main.py
```

## Zasady gry i sterowanie

- LPM (lewy przycisk myszy): zaznaczanie kratki (wypełnienie)
- PPM (prawy przycisk myszy): oznaczanie kratki jako pusta („X”)
- Sprawdź: sprawdza, czy rozwiązanie zgadza się z ukrytym wzorem
- Nowa gra: resetuje bieżący poziom
- Zapisz grę: umożliwia zapis aktualnego stanu
- Menu: powrót do ekranu głównego
- Escape: powoduje wyświetlenie pytania o zapis przy wyjściu

## Obsługa zapisów

- Zapis gry następuje po wybraniu opcji „Zapisz grę” i podaniu nazwy zapisu.
- Przy istnieniu zapisu o tej samej nazwie pojawia się pytanie o jego nadpisanie.
- Zapisy są powiązane z konkretnymi poziomami.
- Dane zapisów przechowywane są w pliku 'save.json'.