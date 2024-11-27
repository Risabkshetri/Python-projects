import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    return pd.read_csv(file_path)

def plot_category_pie(file_path):
    df = load_data(file_path)
    data = df.groupby('Category')['Amount'].sum()
    plt.figure(figsize=(10, 8))
    plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=140)
    plt.title("Expenses by Category")
    plt.savefig("category_pie_chart.png")  # Save the pie chart to a file
    plt.close()  # Close the figure to free memory

def plot_monthly_trend(file_path):
    df = load_data(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.groupby(df['Date'].dt.to_period('M'))['Amount'].sum().reset_index()
    plt.figure(figsize=(10, 8))
    plt.bar(df['Date'].dt.to_timestamp(), df['Amount'])
    plt.title("Monthly Expense Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Expenses")
    plt.xticks(rotation=45)
    plt.savefig("monthly_trend_chart.png")  # Save the bar chart to a file
    plt.close()  # Close the figure to free memory
