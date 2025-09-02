import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Drop duplicates
    df = df.drop_duplicates(['video_id', 'title'])
    df = df.dropna()

    # # Convert dates
    # if "trending_date" in df.columns:
    #     df["trending_date"] = pd.to_datetime(df["trending_date"], errors="coerce")

    # if "publish_time" in df.columns:
    #     df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")

    # Fill NaN in tags with empty string
    if "tags" in df.columns:
        df["tags"] = df["tags"].fillna("")

    # Convert numeric columns safely
    for col in ["views", "likes", "dislikes", "comment_count"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)

    return df
