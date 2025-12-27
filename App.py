import json
from datetime import datetime

DATA_FILE = "expenses.json"


def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def add_expense():
    try:
        amount = float(input("Amount spent: ₹"))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    category = input("Category (e.g. Food, Travel, Bills): ").strip()
    note = input("Note (optional): ").strip()
    date = datetime.now().strftime("%Y-%m-%d")

    new_entry = {"amount": amount, "category": category, "note": note, "date": date}

    expenses = load_data()
    expenses.append(new_entry)
    save_data(expenses)
    print(" Expense saved!")


def view_expenses():
    expenses = load_data()
    if not expenses:
        print("No expense records found yet.")
        return

    print("\n--- All Expenses ---")
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. ₹{e['amount']} | {e['category']} | {e['note']} | {e['date']}")


def total_spent():
    expenses = load_data()
    total = sum(item["amount"] for item in expenses)
    print(f"\n💰 Total Spent: ₹{total}")


def by_category():
    category = input("Enter category to filter: ").strip().lower()
    expenses = load_data()
    filtered = [e for e in expenses if e["category"].lower() == category]

    if not filtered:
        print("No expenses found in that category.")
        return

    print(f"\n--- Expenses in '{category.title()}' ---")
    for e in filtered:
        print(f"₹{e['amount']} | {e['note']} | {e['date']}")


def monthly_report():
    month = input("Enter month (YYYY-MM): ").strip()
    expenses = load_data()
    month_total = sum(e["amount"] for e in expenses if e["date"].startswith(month))
    print(f"📅 Total for {month}: ₹{month_total}")


def main():
    while True:
        print("\n=== Expense Manager ===")
        print("1) Add Expense")
        print("2) View All")
        print("3) Total Spent")
        print("4) Filter by Category")
        print("5) Monthly Report")
        print("6) Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_spent()
        elif choice == "4":
            by_category()
        elif choice == "5":
            monthly_report()
        elif choice == "6":
            print("Exiting... Have a good day!")
            break
        else:
            print(" Invalid choice, please try again.")


if __name__ == "__main__":
    main()
