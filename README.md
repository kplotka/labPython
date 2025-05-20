# Klasyfikacja koktajli na podstawie składników

Projekt polega na rozwiązaniu dwóch niezależnych problemów klasyfikacyjnych z wykorzystaniem sztucznych sieci neuronowych (MLP) przy użyciu `scikit-learn`.

---

## Problem 1 – Klasyfikacja typu smakowego

### Cel:
Na podstawie składników koktajlu określić, czy jest on:
- słodki
- słodko-kwaśny
- wytrawny

### Dane wejściowe:
Składniki z kolumn `Składnik 1–4` zostały zakodowane w postaci one-hot.

### Dane wyjściowe:
Kolumna `Typ` zawierająca typ smakowy.

### Modele:
- Model 1: 1 warstwa ukryta (32 neurony), `relu`
- Model 2: 2 warstwy (64, 32), `tanh`
- Model 3: 3 warstwy (128, 64, 32), `relu`, `alpha=0.01`

### Wyniki:
Każdy model został oceniony na podstawie:
- Accuracy (dokładność na zbiorze testowym)
- Macierzy pomyłek (confusion matrix)

**Najlepszy model**: Model 1 (1x32 relu) – najwyższa dokładność i stabilne wyniki

---

## Problem 2 – Klasyfikacja poziomu alkoholu (ABV)

### Cel:
Na podstawie składników określić, czy koktajl jest:
- **low ABV** (lekki)
- **high ABV** (mocny)

### Dane wejściowe:
Te same składniki zakodowane one-hot.

### Dane wyjściowe:
Ręcznie dodana kolumna `Abv` (low / high), oceniona na podstawie wiedzy barmańskiej o składnikach.

### Modele:
- Model 1: 1 warstwa (16 neuronów), `logistic`
- Model 2: 2 warstwy (32, 16), `relu`, `solver=lbfgs`
- Model 3: 3 warstwy (64, 32, 16), `tanh`, `alpha=0.001`

### Wyniki:
Analogiczne jak w Problemie 1.

**Najlepszy model**: Model 3 (3x tanh + alpha=0.001)

---

## Metryki skuteczności

Dla każdego modelu zostały zaprezentowane:
- **Accuracy**
- **Macierz błędów (confusion matrix)**

Ze względu na wykorzystanie `MLPClassifier`, krzywe uczenia i test loss nie zostały wygenerowane, co jest zgodne z ograniczeniami tej biblioteki.

---

## Wnioski

Projekt pokazuje, że:
- Składniki koktajli zawierają wystarczająco dużo informacji, aby skutecznie klasyfikować typ smakowy i poziom alkoholu,
- Nawet proste modele MLP mogą dawać wysoką skuteczność,
- Architektura modelu (liczba warstw, aktywacje, solver) ma wyraźny wpływ na jakość predykcji.

---

## Struktura projektu

```
├── preprocessing.py
├── problem1_models.py
├── problem1_train.py
├── problem2_models.py
├── problem2_train.py
├── cocktails.csv
├── README.md
```


---

## ✅ Wymagania

- `Python 3.x`
- `scikit-learn`
- `pandas`
- `matplotlib`
- `seaborn`
