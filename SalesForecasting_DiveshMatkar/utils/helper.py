import joblib

from config import MODEL_DIR


def save_model(model, filename):

    path = MODEL_DIR / filename

    joblib.dump(model, path)

    print(f"Model Saved -> {path}")


def load_model(filename):

    path = MODEL_DIR / filename

    return joblib.load(path)