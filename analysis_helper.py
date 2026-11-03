import pandas as pd

AGE_BINS = [0, 17, 34, 49, 64, 120]
AGE_LABELS = ["Under 18", "18-34", "35-49", "50-64", "65+"]

def load_data(path="data/healthcare_clean.csv"):
    """Load the cleaned data and add analysis columns."""
    df = pd.read_csv(path, parse_dates=["Date of Admission", "Discharge Date"])

    df["Length of Stay"] = (df["Discharge Date"] - df["Date of Admission"]).dt.days
    df["Age Group"] = pd.cut(df["Age"], bins=AGE_BINS, labels=AGE_LABELS)
    df["Admission Year"] = df["Date of Admission"].dt.year
    df["Admission Month"] = df["Date of Admission"].dt.to_period("M")

    return df