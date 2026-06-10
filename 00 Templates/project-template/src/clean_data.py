"""Reusable cleaning script template for analytics projects."""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Apply project-specific cleaning steps."""
    cleaned = df.copy()
    cleaned.columns = cleaned.columns.str.strip().str.lower().str.replace(" ", "_")
    return cleaned


if __name__ == "__main__":
    input_file = RAW_DIR / "input.csv"
    output_file = PROCESSED_DIR / "cleaned_data.csv"

    data = pd.read_csv(input_file)
    cleaned_data = clean_data(data)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    cleaned_data.to_csv(output_file, index=False)
