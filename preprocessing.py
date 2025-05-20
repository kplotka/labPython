import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer, LabelEncoder

def load_data_and_labels(csv_path, label_column):
    df = pd.read_csv(csv_path)
    ingredient_cols = ["Składnik 1", "Składnik 2", "Składnik 3", "Składnik 4"]
    df[ingredient_cols] = df[ingredient_cols].fillna("")
    df["All_Ingredients"] = df[ingredient_cols].values.tolist()
    df["All_Ingredients"] = df["All_Ingredients"].apply(
        lambda x: [i.strip().lower() for i in x if i.strip() != ""]
    )
    mlb = MultiLabelBinarizer()
    X = mlb.fit_transform(df["All_Ingredients"])
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(df[label_column])
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    return X_train, X_test, y_train, y_test