import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, confusion_matrix
from preprocessing import load_data_and_labels
from problem2_models import build_model_1, build_model_2, build_model_3

def train(model_fn, X_train, X_test, y_train, y_test, name):
    model = model_fn()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"{name} - Test Accuracy: {acc * 100:.2f}%")
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(5, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f'{name} - Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = load_data_and_labels("cocktails.csv", "Abv")

    results = []

    for build_fn, name in [
        (build_model_1, "Model 1 (1x16 logistic)"),
        (build_model_2, "Model 2 (2x relu + lbfgs)"),
        (build_model_3, "Model 3 (3x tanh + alpha=0.001)")
    ]:
        model = build_fn()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        results.append((name, acc))

        print(f"\n{name} - Test Accuracy: {acc * 100:.2f}%")
        cm = confusion_matrix(y_test, y_pred)
        plt.figure(figsize=(5, 4))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.title(f'{name} - Confusion Matrix')
        plt.xlabel('Predicted')
        plt.ylabel('Actual')
        plt.tight_layout()
        plt.show()

    best_name, best_acc = max(results, key=lambda x: x[1])
    print(f"\nNajlepszy model: {best_name} ({best_acc * 100:.2f}%)")