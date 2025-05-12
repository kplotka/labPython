# Cocktail Classification Model

Projekt polega na klasyfikacji typów koktajli na podstawie składników, które zawierają. Wykorzystuje szereg klasyfikatorów maszynowego uczenia, takich jak **Random Forest**, **Gradient Boosting**, **XGBoost**, **Logistic Regression** oraz **Gaussian Naive Bayes**.

## Wymagania

Aby uruchomić projekt, należy mieć zainstalowane następujące biblioteki:

- `pandas` - do pracy z danymi w formie tabel.
- `numpy` - do obliczeń numerycznych.
- `scikit-learn` - do trenowania modeli maszynowego uczenia i przetwarzania danych.
- `xgboost` - do trenowania modelu XGBoost.
- `seaborn` i `matplotlib` - do wizualizacji wyników.

### Instalacja

Aby zainstalować wymagane biblioteki, użyj poniższego polecenia:

```bash
pip install pandas numpy scikit-learn xgboost seaborn matplotlib
```
## Struktura projektu

### Pliki

- `cocktails.csv`: Plik zawierający dane dotyczące składników koktajli oraz ich typów.
- `model.py`: Główny plik z kodem, który trenuje modele klasyfikacyjne.
- `README.md`: Ten plik z dokumentacją.

### Przykładowa struktura danych (`cocktails.csv`)

Plik CSV zawiera następujące kolumny:
- **Składnik 1**: Pierwszy składnik koktajlu.
- **Składnik 2**: Drugi składnik koktajlu.
- **Składnik 3**: Trzeci składnik koktajlu.
- **Składnik 4**: Czwarty składnik koktajlu.
- **Typ**: Typ koktajlu (np. "Margarita", "Mojito").

### Inżynieria cech

Wramach przygotowania danych dodana jest następująca cecha:
- **składniki_długość**: Długość połączonych nazw składników, która może wpływać na typ koktajlu.

## Opis algorytmu

Skrypt wykonuje następujące kroki:

1. **Wczytanie danych**: Plik CSV jest wczytywany przy pomocy `pandas`.
2. **Obsługa brakujących danych**: Brakujące dane są wypełniane pustymi ciągami tekstowymi.
3. **Inżynieria cech**: Tworzymy nową cechę, która reprezentuje długość wszystkich składników w koktajlu.
4. **Kodowanie etykiet i OneHot Encoding**:
- Etykiety koktajli (np. "Margarita") są kodowane na liczby za pomocą `LabelEncoder`.
- Składniki koktajli są kodowane za pomocą `OneHotEncoder`, co zamienia je w wektory binarne.
5. **Podział na dane treningowe i testowe**: Zbiór danych jest dzielony na 70% dane treningowe i 30% dane testowe.
6. **Normalizacja danych**: Używamy `StandardScaler` do standaryzacji danych, co zapewnia, że każda cecha ma średnią 0 i odchylenie standardowe 1.
7. **Trenowanie modeli**:
- Modele klasyfikacyjne (Random Forest, Gradient Boosting, Logistic Regression, XGBoost, Gaussian Naive Bayes) są trenowane na danych treningowych.
- Dla modelu XGBoost optymalizujemy hiperparametry za pomocą `GridSearchCV`.
8. **Ocena wyników**:
- Dokładność każdego modelu jest obliczana za pomocą `accuracy_score`.
- Tworzona jest macierz pomyłek, która ilustruje, jak model radził sobie z klasyfikacją poszczególnych typów koktajli.

## Użycie

Po uruchomieniu skryptu modele są trenowane, a wyniki są wyświetlane w postaci:
- Dokładności `(accuracy_score)` dla każdego modelu.
- Macierzy pomyłek dla każdego modelu, która przedstawia liczbę prawidłowych i błędnych klasyfikacji dla każdego typu koktajlu.

### Uruchomienie skryptu

Aby uruchomić skrypt, wystarczy wykonać następujące polecenie w terminalu:

```bash
python model.py
```
### Wyniki

Po uruchomieniu skryptu, otrzymasz wyniki treningu dla każdego modelu w postaci dokładności oraz wykresów z macierzami pomyłek.

Przykład wyników:

```textmate
Random Forest - Dokładność: 85.30%
Gradient Boosting - Dokładność: 83.20%
Logistic Regression - Dokładność: 79.50%
XGBoost - Dokładność: 86.10%
Gaussian Naive Bayes - Dokładność: 78.60%
```

### Wizualizacja

Skrypt generuje wykresy z macierzami pomyłek, które pokazują, jak dobrze każdy model klasyfikuje poszczególne typy koktajli.

## Optymalizacja XGBoost

Do optymalizacji modelu XGBoost wykorzystany jest `GridSearchCV`, który przeprowadza automatyczne testowanie różnych wartości parametrów, takich jak liczba drzew `(n_estimators)`, głębokość drzew `(max_depth)`, współczynnik uczenia `(learning_rate)`, oraz inne.

Przykład optymalnych parametrów:

```yaml
XGBoost - Najlepsze parametry: {'colsample_bytree': 0.8, 'learning_rate': 0.01, 'max_depth': 5, 'n_estimators': 200, 'subsample': 1.0}
```

## Podsumowanie

W tym projekcie stworzony został model klasyfikacyjny, który przewiduje typ koktajlu na podstawie składników. Użyto kilku klasyfikatorów maszynowego uczenia i przeprowadzona została optymalizacja hiperparametrów dla modelu XGBoost, uzyskując dobre wyniki klasyfikacji. Model można łatwo zaadaptować do różnych zestawów danych o koktajlach.

## Licencja

Ten projekt jest objęty licencją MIT. Możesz go dowolnie używać i modyfikować.