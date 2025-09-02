import os
import pandas as pd

def load_data():
    # Path to your data folder
    data_path = os.path.join(os.path.dirname(__file__), "..", "data")

    # Print what files are inside (debugging)
    print("Files in data folder:", os.listdir(data_path))

    # Load datasets for 3 countries
    us = pd.read_csv(os.path.join(data_path, "USvideos.csv"))
    in_data = pd.read_csv(os.path.join(data_path, "INvideos.csv"))
    gb = pd.read_csv(os.path.join(data_path, "GBvideos.csv"))

    # Add country column
    us["country"] = "US"
    in_data["country"] = "IN"
    gb["country"] = "GB"

    # Combine all
    df = pd.concat([us, in_data, gb], ignore_index=True)

    return df
