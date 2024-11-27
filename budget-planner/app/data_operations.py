import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def add_expense(file_path, date, category, description, amount):
    new_data = {'Date': date, 'Category': category, 'Description': description, 'Amount': amount}
    df = pd.read_csv(file_path)
    df = df._append(new_data, ignore_index=True)
    df.to_csv(file_path, index=False)

def delete_expense(file_path, row_index):
    df = pd.read_csv(file_path)
    df = df.drop(index=row_index)
    df.to_csv(file_path, index=False)
