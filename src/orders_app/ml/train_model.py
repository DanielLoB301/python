from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib


def main():
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_PATH = BASE_DIR / "data" / "customers.csv"

    df = pd.read_csv(DATA_PATH)

    X = df[["age", "income"]]
    y = df["purchased"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print(f"Accuracy: {accuracy}")

    MODEL_PATH = BASE_DIR / "data" / "model.joblib"
    joblib.dump(model, MODEL_PATH)

    print(f"Modelo guardado en {MODEL_PATH}")


if __name__ == "__main__":
    main()