# Mowa Kwiatów – strona Django inspirowana romantyzmem

**Mowa Kwiatów** to minimalistyczna aplikacja stworzona w Django, która umożliwia użytkownikom tworzenie analogowego bukietu na podstawie wiktoriańskiego języka kwiatów. To narzędzie powrotu do zapomnianego rytuału przekazywania emocji i intencji za pomocą symboliki florystycznej.

---

## Spis treści

- [Opis](#opis)
- [Funkcjonalności](#funkcjonalności)
- [Technologie](#technologie)
- [Instalacja](#instalacja)
- [Obsługa błędów](#obsługa-błędów)

---

## Opis

W XIX wieku bukiety miały ukryte znaczenia. Kwiaty przekazywały miłość, żal, wdzięczność lub zazdrość. Ta aplikacja pomaga stworzyć taki bukiet — nie podążając za trendami, lecz za osobistym przekazem, jaki chcemy wysłać.

---

## Funkcjonalności

- Rejestracja, logowanie, wylogowywanie użytkowników
- Strona główna z wprowadzeniem do języka kwiatów
- Słownik kwiatów alfabetyczny z ich symboliką
- Planer bukietu:
  - filtrowanie kwiatów po kategoriach (np. miłość, przyjaźń, żałoba)
  - dodawanie wybranych kwiatów do koszyka
- Koszyk w formie wizualnego bukietu:
  - podgląd symboliki wybranych kwiatów
  - usuwanie pojedynczych kwiatów lub całego bukietu
  - zapis bukietu z nadaną nazwą (dla zalogowanych)
- Moje bukiety:
  - lista zapisanych bukietów
  - możliwość ich podglądu i usunięcia
- Delikatna, minimalistyczna szata graficzna z ilustracjami
- Obsługa ikon kwiatów oraz personalizacji wyglądu

---

## Technologie

- Django 4.x
- Python 3.9+
- HTML5 + CSS3 (własne style inspirowane Tailwindem)
- Bootstrap 5 (opcjonalnie)
- Django templating engine
- Sesje i system użytkowników Django

---

## Instalacja lokalna

1. **Klonuj repozytorium:**
   ```bash
   git clone https://github.com/kplotka/labPython.git
   cd mowa_kwiatow
   ```
   
2. **Utwórz środowisko wirtualne:**
    ```bash
    python -m venv .venv
    .venv\Scripts\activate  # Windows
    source .venv/bin/activate  # Linux/macOS
    ```
   
3. **Zainstaluj zależności:**
    ```bash
   pip install -r requirements.txt
    ```
   
4. **Uruchom migracje:**
    ```bash
   python manage.py migrate
    ```

5. **Uruchom serwer:**
    ```bash
   python manage.py runserver
    ```
   
## Obsługa błędów i wyjątkowych sytuacji

Aplikacja obsługuje nietypowe przypadki i błędy użytkownika:

- Brak uprawnień: dostęp do zapisu lub podglądu bukietów tylko po zalogowaniu
- Pusty koszyk: brak możliwości zapisu; użytkownik otrzymuje komunikat
- Brak nazwy bukietu: formularz przypomina o obowiązkowym polu
- Podwójne dodanie kwiatu: unikalne ID w sesji – brak duplikatów
- Błędne dane logowania: system wyświetla adekwatny komunikat