# CastingHub

Casting Hub to nowoczesny, minimalistyczny portal castingu stworzony w Django. Projekt umożliwia rejestrację użytkowników jako modeli lub casting directorów, a następnie:

- **Modele:** mogą przeglądać oferty castingu oraz aplikować na nie. Po zaakceptowaniu aplikacji wyświetlane są dane kontaktowe casting directora.
- **Casting directorzy:** mogą dodawać, edytować i usuwać oferty castingu oraz zarządzać zgłoszeniami (aplikacjami) od modeli.
- **Profile użytkowników:** oddzielne widoki profili dla modeli i directorów, z możliwością edycji i wyświetlania zdjęć profilowych.
- **Niestandardowe polecenie Django:** `clear_expired_offers` usuwa oferty, których data zakończenia już minęła.

## Spis treści

- [Funkcjonalności](#funkcjonalności)
- [Technologie](#technologie)
- [Instrukcje użytkowania](#instrukcje-użytkowania)
- [Źródła](#źródła)
- [Autorzy](#autorzy)

## Funkcjonalności

- **Rejestracja i logowanie:** Użytkownicy tworzą konto wybierając rolę (model lub casting director). W zależności od wybranej roli tworzony jest odpowiedni profil (ModelProfile lub DirectorProfile).
- **Oferty castingu:**  
  - Casting directorzy mogą dodawać, edytować i usuwać oferty castingu.  
  - Modele mogą przeglądać oferty i aplikować – przycisk „Aplikuj” jest ukryty, jeśli aplikacja została już złożona.
- **Aplikacje:** Modele składają aplikacje na oferty, a directorzy mogą zarządzać zgłoszeniami, zmieniać status aplikacji (np. na "Accepted" lub "Rejected") oraz przeglądać profile aplikujących modeli.
- **Profile użytkowników:** Oddzielne widoki profili dla modeli i directorów, zawierające dane osobowe, zdjęcia profilowe i możliwość edycji.
- **Niestandardowe polecenie:** Polecenie `clear_expired_offers` usuwa oferty castingu, których data zakończenia już minęła.

## Technologie

- Python 3.13.1  
- Django 5.1.7  
- HTML/CSS – minimalistyczny, nowoczesny design inspirowany estetyką Apple  
- Git – kontrola wersji

## Instrukcja użytkowania

- **Dla modeli:** Po rejestracji i zalogowaniu, modele przeglądają oferty castingu, aplikują na nie i w swoim profilu śledzą status aplikacji. Po zaakceptowaniu aplikacji wyświetlane są dane kontaktowe casting directora.
- **Dla casting directorów:** Casting directorzy dodają oferty castingu, edytują i usuwają je oraz zarządzają zgłoszeniami od modeli.

## Źródła

- [Django Documentation](https://docs.djangoproject.com/)
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Django Template Language](https://docs.djangoproject.com/en/5.1/topics/templates/)
- ChatGPT (debugowanie + clean code)