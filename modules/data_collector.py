import pandas as pd
import json

def collect_usage_data(csv_path):
    return pd.read_csv(csv_path)

def load_plans(json_path):
    with open(json_path) as f:
        return json.load(f)
