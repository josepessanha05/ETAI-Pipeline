import yaml
from src.data import load_data
from src.preprocessing import clean_dataset

cfg = yaml.safe_load(open("config_adult.yaml"))
df = clean_dataset(load_data(cfg["data"]["path"]), cfg["diagnostics"])

for col, expected in [("workclass", 379), ("occupation", 381), ("native_country", 86)]:
    n_missing = int(df[col].isna().sum())
    n_question = int((df[col] == "?").sum())
    print(f"{col:<15s} missing={n_missing} (expected {expected})   '?' left={n_question}")
    print(df[col].value_counts(dropna=False).head(4).to_string(), "\n")