import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_top_categories(df):
    output_path = os.path.join(os.path.dirname(__file__), "..", "demo")

    # Group and count top categories
    top_cats = df["category_name"].value_counts().head(10)
    plt.figure(figsize=(15,7))
    sns.barplot(x=top_cats.index, y=top_cats.values, palette="viridis")
    plt.title("Top 10 Trending Categories")
    plt.xlabel("Category ID")
    plt.ylabel("Count")
    plt.xticks(rotation=90, ha="right")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "top_categories.png"))
    plt.close()
