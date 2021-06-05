import joblib
import numpy as np
from pathlib import Path

from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_boston


class Model:
    def __init__(self, model_path: str = None):
        self._model = None
        self._model_path = model_path
        self.load()

    def predict(self, X: np.ndarray) -> np.ndarray:
        return self._model.predict(X)

    def load(self):
        try:
            self._model = joblib.load(self._model_path)
        except:
            self._model = None
        return self


model_path = Path(__file__).parent / "model.joblib"
n_features = load_boston(return_X_y=True)[0].shape[1]
model = Model(model_path)


def get_model():
    return model


if __name__ == "__main__":
    X, y = load_boston(return_X_y=True)
    model.train(X, y)
    model.save()