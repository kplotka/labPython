from sklearn.neural_network import MLPClassifier

def build_model_1():
    return MLPClassifier(hidden_layer_sizes=(32,), activation='relu', max_iter=1000, random_state=42)

def build_model_2():
    return MLPClassifier(hidden_layer_sizes=(64, 32), activation='tanh', max_iter=1000, random_state=42)

def build_model_3():
    return MLPClassifier(hidden_layer_sizes=(128, 64, 32), activation='relu', alpha=0.01, max_iter=1000, random_state=42)