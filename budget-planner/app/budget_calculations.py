import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def calculate_total(file_path):
    df = load_data(file_path)
    return df['Amount'].sum()

def calculate_by_category(file_path):
    df = load_data(file_path)
    return df.groupby('Category')['Amount'].sum().to_dict()
