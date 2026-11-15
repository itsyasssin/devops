"""Train a tiny regression model and dump it to disk."""
import json
import joblib
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split


def make_data(n=1000, seed=42):
    rng = np.random.default_rng(seed)
    size = rng.uniform(30, 250, n)          # m2
    bedrooms = rng.integers(1, 6, n)
    age = rng.uniform(0, 80, n)             # years
    price = 50_000 + 2_500 * size + 10_000 * bedrooms - 800 * age + rng.normal(0, 15_000, n)
    return np.column_stack([size, bedrooms, age]), price


def train(model_path="model.joblib", metrics_path="metrics.json"):
    X, y = make_data()
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=0)
    model = LinearRegression().fit(X_tr, y_tr)
    metrics = {"r2": round(r2_score(y_te, model.predict(X_te)), 4)}
    joblib.dump(model, model_path)
    with open(metrics_path, "w") as f:
        json.dump(metrics, f)
    return metrics


if __name__ == "__main__":
    print(train())
