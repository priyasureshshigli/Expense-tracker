import datetime
import json
import os

FILENAME = "expenses.json"

def load_expenses():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open(FILENAME, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ") or str(datetime.date.today())
    category = input("Enter category (food, travel, bills, etc.): ")
    amount = float(input("Enter amount: ₹ "))
    note = input("Enter note (optional): ")

    expenses.append({
        "date": date,
        "category": category,
        "amount": amount,
        "note": note
    })
    save_expenses(expenses)
    print("✅ Expense added successfully!\n")

def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n📋 All Expenses:")
    for exp in expenses:
        print(f"{exp['date']} | ₹{exp['amount']} | {exp['category']} | {exp.get('note', '')}")
    print()

def total_spent(expenses):
    total = sum(exp['amount'] for exp in expenses)
    print(f"\n💰 Total Spent: ₹{total:.2f}\n")

def main():
    expenses = load_expenses()

    while True:
        print("=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Total Spending")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            total_spent(expenses)
        elif choice == '4':
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()