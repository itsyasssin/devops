from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    assert client.get("/health").json()["status"] == "ok"


def test_predict():
    r = client.post("/predict", json={"size": 100, "bedrooms": 3, "age": 10})
    assert r.status_code == 200
    assert 200_000 < r.json()["price"] < 400_000


def test_validation():
    assert client.post("/predict", json={"size": -1, "bedrooms": 3, "age": 1}).status_code == 422


def test_ui():
    assert "House price" in client.get("/").text
