from train import train


def test_model_quality(tmp_path):
    m = train(tmp_path / "m.joblib", tmp_path / "m.json")
    assert m["r2"] > 0.95, f"model too weak: {m}"
