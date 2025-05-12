import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("cocktails.csv")
df = df.fillna("")
df['składniki_długość'] = df[['Składnik 1', 'Składnik 2', 'Składnik 3', 'Składnik 4']].apply(lambda row: len(' '.join(row)), axis=1)

encoder = LabelEncoder()
y = encoder.fit_transform(df["Typ"])

ingredients = df[["Składnik 1", "Składnik 2", "Składnik 3", "Składnik 4"]]
onehot_encoder = OneHotEncoder(sparse_output=False)
ingredients_encoded = onehot_encoder.fit_transform(ingredients)

X = np.concatenate([ingredients_encoded, df[['składniki_długość']].values], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

models = {
    "Random Forest": RandomForestClassifier(random_state=42),
    "Gradient Boosting": GradientBoostingClassifier(random_state=42),
    "Logistic Regression": LogisticRegression(max_iter=10000, random_state=42),
    "XGBoost": XGBClassifier(random_state=42),
    "Gaussian Naive Bayes": GaussianNB()
}

param_grid_xgb = {
    'n_estimators': [100, 200, 300],
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.05, 0.1],
    'subsample': [0.8, 1.0],
    'colsample_bytree': [0.8, 1.0]
}

def train_and_plot(model, X_train_scaled, y_train, X_test_scaled, y_test, model_name, param_grid=None):
    if param_grid:
        grid_search = GridSearchCV(model, param_grid, cv=3, n_jobs=-1, verbose=0)
        grid_search.fit(X_train_scaled, y_train)
        best_model = grid_search.best_estimator_
        print(f"{model_name} - Najlepsze parametry: {grid_search.best_params_}")
    else:
        best_model = model
        best_model.fit(X_train_scaled, y_train)

    y_pred = best_model.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    print(f"{model_name} - Dokładność: {acc * 100:.2f}%")

    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False,
                xticklabels=encoder.classes_, yticklabels=encoder.classes_)
    plt.title(f"{model_name} - Macierz Pomyłek")
    plt.show()

for model_name, model in models.items():
    if model_name == "XGBoost":
        train_and_plot(model, X_train_scaled, y_train, X_test_scaled, y_test, model_name, param_grid_xgb)
    else:
        train_and_plot(model, X_train_scaled, y_train, X_test_scaled, y_test, model_name)