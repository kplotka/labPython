import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score
from preprocessing import load_and_preprocess_data
from models import build_model_1, build_model_2, build_model_3

def train_and_evaluate_model(build_fn, model_name, X_train, X_test, y_train, y_test):
    model = build_fn()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print(f"\n{model_name} - Test Accuracy: {acc * 100:.2f}%")

    cm = confusion_matrix(y_test, y_pred)

    plt.figure(figsize=(5, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f'{model_name} - Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    X_train, X_test, y_train, y_test, ingredient_names, label_encoder = load_and_preprocess_data("cocktails.csv")

    train_and_evaluate_model(build_model_1, "Model 1 (1x32 relu)", X_train, X_test, y_train, y_test)
    train_and_evaluate_model(build_model_2, "Model 2 (2x tanh)", X_train, X_test, y_train, y_test)
    train_and_evaluate_model(build_model_3, "Model 3 (3x relu, alpha=0.01)", X_train, X_test, y_train, y_test)