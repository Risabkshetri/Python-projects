import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from app.data_operations import load_data, add_expense, delete_expense
from app.budget_calculations import calculate_total, calculate_by_category
from app.visualization import plot_category_pie, plot_monthly_trend

FILE_PATH = "data/data.csv"

def main():
    while True:
        print("\n=== Budget Planner ===")
        print("1. View Expenses")
        print("2. Add Expense")
        print("3. Delete Expense")
        print("4. Show Total")
        print("5. Visualize Expenses")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print(load_data(FILE_PATH))
        elif choice == '2':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            add_expense(FILE_PATH, date, category, description, amount)
        elif choice == '3':
            row = int(input("Enter row index to delete: "))
            delete_expense(FILE_PATH, row)
        elif choice == '4':
            print("Total Expenses:", calculate_total(FILE_PATH))
            print("Category-wise Breakdown:", calculate_by_category(FILE_PATH))
        elif choice == '5':
            plot_category_pie(FILE_PATH)
            plot_monthly_trend(FILE_PATH)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
