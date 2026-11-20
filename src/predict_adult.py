"""Predict a label-free file with the final refit pipeline."""
import os
import pandas as pd
from src.data import load_data
from src.preprocessing import clean_dataset, split_features_target


def predict_new(pipeline, config: dict, out_path: str, threshold: float = 0.5) -> int:
    raw = load_data(config["data"]["new_path"])
    clean = clean_dataset(raw, config["diagnostics"])          # no drop_duplicate_rows here
    X_new, _, _ = split_features_target(
        clean, config["data"], config["preprocessing"].get("mnar_indicator_sources", []))
    proba = pipeline.predict_proba(X_new)[:, 1]
    id_col = config["diagnostics"]["id_column"]
    out = pd.DataFrame({id_col: raw[id_col].values,
                        "probability": proba,
                        "prediction": (proba >= threshold).astype(int)})
    assert len(out) == len(raw), "every row needs a prediction"
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    out.to_csv(out_path, index=False)
    return len(out)