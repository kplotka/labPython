# Klasyfikacja koktajli na podstawie składników

Projekt polega na klasyfikacji koktajli na trzy typy: **słodki**, **słodko-kwaśny** oraz **wytrawny**, na podstawie ich składników. Został zrealizowany przy użyciu klasycznych sieci neuronowych (`MLPClassifier`) dostępnych w bibliotece `scikit-learn`.

## Struktura Projektu

```
├── preprocessing.py # Wczytanie i przetwarzanie danych z cocktails.csv
├── models.py # Definicje trzech wariantów sieci neuronowych
├── train_and_evaluate.py # Trening, ewaluacja i wizualizacja wyników
├── cocktails.csv # Zbiór danych wejściowych (gotowy plik)
└── __init__.py # Plik techniczny (może być pusty)
```

## Dane wejściowe

Zbiór danych `cocktails.csv` zawiera:
- nazwę koktajlu,
- 1–4 składniki,
- etykietę typu koktajlu (klasa).

Dane są przetwarzane do postaci binarnej (one-hot) — każdy składnik jest reprezentowany jako osobna cecha wejściowa (kolumna 0/1).

## Modele

W projekcie zdefiniowano trzy warianty klasycznej sieci neuronowej typu MLP:

- **Model 1:** jedna warstwa ukryta (32 neurony, `relu`)
- **Model 2:** dwie warstwy ukryte (64 i 32 neurony, `tanh`)
- **Model 3:** trzy warstwy ukryte (128, 64, 32 neurony, `relu`, `alpha=0.01`)

Każdy model trenowany jest na tym samym zbiorze treningowym.

## Wyniki

Każdy model został oceniony na zbiorze testowym, a wyniki przedstawiono jako:

- dokładność klasyfikacji (w procentach),
- macierz pomyłek (confusion matrix).

Przykładowe wyniki:

```
Model 1 (1x32 relu) - Test Accuracy: 93.00%
Model 2 (2x tanh) - Test Accuracy: 89.00%
Model 3 (3x relu, alpha=0.01) - Test Accuracy: 91.00%
```

## Uruchomienie

1. Upewnij się, że plik `cocktails.csv` znajduje się w tym samym folderze co pliki `.py`.
2. Uruchom program:
```bash
python train_and_evaluate.py
```

## Wymagane biblioteki

- `pandas`
- `numpy`
- `scikit-learn`
- `matplotlib`
- `seaborn`

Można je zaintsalować za pomocą:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```