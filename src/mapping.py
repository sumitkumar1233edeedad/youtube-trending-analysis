import pandas as pd
import json
import os

def mapping(df: pd.DataFrame) -> pd.DataFrame:
    # Path to ../data folder
    data_path = os.path.join(os.path.dirname(__file__), "..", "data")

    # Load JSON file
    with open(os.path.join(data_path, "US_category_id.json"), "r") as f:
        data = json.load(f)

    # Extract category mapping (id → name)
    category_mapping = {}
    for item in data["items"]:
        category_mapping[int(item["id"])] = item["snippet"]["title"]

    # Map to your DataFrame
    df["category_name"] = df["category_id"].map(category_mapping)

    return df
    