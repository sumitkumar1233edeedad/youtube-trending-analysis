from load_data import load_data
from data_cleaning import clean_data
from visualization import plot_top_categories
from mapping import mapping
import pandas as pd
import os

def main():
    print("📥 Loading data...")
    df = load_data()
    
    folder_path = "C:/Users/sumit/OneDrive/Desktop/project work/youtube-trending-analysis/data/processed"

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_path = os.path.join(folder_path, "combined.csv")
    df.to_csv(file_path, index=False) 
    

    print("🧹 Cleaning data...")
    df = clean_data(df)
    file_path = os.path.join(folder_path, "combined_clean.csv")
    df.to_csv(file_path, index=False) 
    
    
    df = mapping(df)
    file_path = os.path.join(folder_path, "combined_mapping.csv")
    df.to_csv(file_path, index=False) 
    
    
    
    print("📊 Generating visualizations...")
    plot_top_categories(df)

    print("✅ Done! Check the 'demo/' folder for charts.")

if __name__ == "__main__":
    main()
