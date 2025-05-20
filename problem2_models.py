from sklearn.neural_network import MLPClassifier

def build_model_1():
    return MLPClassifier(hidden_layer_sizes=(16,), activation='logistic', max_iter=1500, solver='adam', random_state=42)

def build_model_2():
    return MLPClassifier(hidden_layer_sizes=(32, 16), activation='relu', max_iter=1500, solver='lbfgs', random_state=42)

def build_model_3():
    return MLPClassifier(hidden_layer_sizes=(64, 32, 16), activation='tanh', alpha=0.001, max_iter=1500, solver='adam', random_state=42)