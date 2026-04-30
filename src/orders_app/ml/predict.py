from pathlib import Path
import joblib
import numpy as np


def main():
    BASE_DIR = Path(__file__).resolve().parent.parent
    MODEL_PATH = BASE_DIR / "data" / "model.joblib"

    model = joblib.load(MODEL_PATH)

    new_customer = np.array([[30, 40000]])
    prediction = model.predict(new_customer)

    print("Predicción:", prediction[0])


if __name__ == "__main__":
    main()