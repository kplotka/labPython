# CastingHub

## Spis treści
- [Wprowadzenie](#wprowadzenie)
- [Architektura projektu](#architektura-projektu)
- [Modele danych](#modele-danych)
- [Widoki i logika biznesowa](#widoki-i-logika-biznesowa)
- [Szablony i front-end](#szablony-i-front-end)
- [Niestandardowe polecenia](#niestandardowe-polecenia)
- [Instrukcje deweloperskie](#instrukcje-deweloperskie)
- [Źródła](#źródła)
- [Podsumowanie](#podsumowanie)

## Wprowadzenie
Casting Hub to minimalistyczny portal castingu stworzony w Django. Projekt umożliwia rejestrację użytkowników jako modele lub casting directorzy. Modele przeglądają oferty castingu, aplikują na nie, a casting directorzy dodają oferty i zarządzają zgłoszeniami. Projekt został zaprojektowany z myślą o przejrzystości, modularności oraz skalowalności.

## Architektura projektu
Projekt oparty jest na frameworku Django i składa się z następujących elementów:
- **Modele:** Odpowiadają za przechowywanie danych w bazie, definiowane w pliku `models.py`.
- **Widoki:** Logika biznesowa i obsługa żądań HTTP, zdefiniowana w `views.py`.
- **Szablony:** Prezentacja danych – HTML i CSS, umieszczone w katalogu `casting/templates/casting/`.
- **Formularze:** Walidacja i przetwarzanie danych wprowadzonych przez użytkownika, znajdują się w `forms.py`.
- **Niestandardowe polecenia:** Polecenia zarządzania (np. usuwanie przeterminowanych ofert) znajdują się w katalogu `casting/management/commands/`.

## Modele danych
Projekt zawiera następujące modele:

### User
Wykorzystywany z Django (django.contrib.auth.models.User).

### ModelProfile
- Relacja OneToOneField z User (`related_name='model_profile'`).
- Pola: `full_name`, `age`, `height`, `weight`, `measurements`, `portfolio_url`, `profile_picture`, `bio`.

### DirectorProfile
- Relacja OneToOneField z User (`related_name='director_profile'`).
- Pola: `full_name`, `agency_name`, `agency_address`, `contact_email`, `contact_phone`, `bio`, `profile_picture`.

### CastingOffer
- Pole `director`: ForeignKey do DirectorProfile (`related_name='casting_offers'`).
- Pola: `title`, `description`, `requirements`, `offer_date`, `location`, `created_at`.

### Application
- Pole `offer`: ForeignKey do CastingOffer (`related_name='applications'`).
- Pole `model_profile`: ForeignKey do ModelProfile (`related_name='applications'`).
- Pola: `message`, `applied_at`, `status`.

Relacje między modelami:
- OneToOneField: Każdy użytkownik ma jeden profil (ModelProfile lub DirectorProfile).
- ForeignKey: Jeden casting director może dodać wiele ofert; jedna oferta może mieć wiele aplikacji; jeden model może aplikować wielokrotnie (na różne oferty).

## Widoki i logika biznesowa
Główne widoki projektu znajdują się w `views.py`:
- **home:** Strona główna.
- **add_casting_offer:** Widok dodawania ofert (tylko dla directorów).
- **offers_list:** Lista ofert castingu – dostępna dla wszystkich użytkowników.
- **offer_detail:** Szczegóły oferty, z dynamicznym wyświetlaniem przycisku „Aplikuj” dla modeli.
- **apply_offer:** Formularz aplikacji dla modeli.
- **register:** Rejestracja użytkowników – tworzenie profilu zależnie od wybranej roli.
- **profile:** Widok profilu użytkownika – oddzielnie dla modeli i directorów.
- **edit_profile:** Edycja profilu.
- **edit_offer:** Edycja oferty (dla directorów).
- **view_applications / manage_applications:** Zarządzanie aplikacjami dla konkretnej oferty (tylko dla directorów).
- **update_application_status:** Zmiana statusu aplikacji (np. akceptacja lub odrzucenie).

Obsługa błędów:
- Widoki wykorzystują `get_object_or_404` do obsługi błędów 404.
- Warunki w widokach sprawdzają, czy użytkownik ma odpowiedni profil, inaczej następuje przekierowanie (np. `redirect('home')`).

## Szablony i front-end
Projekt korzysta z systemu dziedziczenia szablonów w Django:
- **base.html:** Główny szablon zawierający wspólną strukturę (nagłówek, stopka, pasek nawigacyjny, style).
- Pozostałe szablony (home.html, offers_list.html, offer_detail.html, itp.) rozszerzają base.html i definiują bloki `title` i `content`.

Stylizacja opiera się na minimalistycznym, nowoczesnym designie z wykorzystaniem czystej typografii i stonowanej kolorystyki.

## Niestandardowe polecenie
W katalogu `casting/management/commands/clear_expired_offers.py` znajduje się polecenie:
- **clear_expired_offers:** Usuwa oferty castingu, których `offer_date` jest mniejsza niż dzisiejsza data.
  Aby uruchomić polecenie, użyj:
  ```bash
  python manage.py clear_expired_offers
  
## Instrukcje deweloperskie

- **Instalacja:** Sklonuj repozytorium, utwórz wirtualne środowisko, zainstaluj zależności, wykonaj migracje, utwórz superużytkownika i uruchom serwer.
- **Struktura projektu:** Kod jest podzielony na modele (models.py), widoki (views.py), szablony (casting/templates/casting/), formularze (forms.py) oraz niestandardowe polecenia (management/commands).
- **Dodawanie nowych funkcjonalności:** Nowe modele, widoki i szablony należy dodawać zgodnie z zasadą dziedziczenia szablonów i logiki opartej na widokach funkcji.

## Źródła

- [Django Documentation](https://docs.djangoproject.com/)
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Django Template Language](https://docs.djangoproject.com/en/5.1/topics/templates/)
- ChatGPT (debugowanie + clean code)

## Autorzy

Katarzyna Płotka