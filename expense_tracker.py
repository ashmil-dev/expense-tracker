import datetime

# Store expenses in a list
expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount (₹): "))
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expenses.append({"name": name, "amount": amount, "date": date})
    print("✅ Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses yet.\n")
        return
    print("\n📘 Expense List:")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['name']} - ₹{exp['amount']} on {exp['date']}")
    print()

def total_expense():
    total = sum(exp['amount'] for exp in expenses)
    print(f"\n💰 Total Expense: ₹{total}\n")

def main():
    while True:
        print("==== Expense Tracker ====")
        print("1️⃣ Add Expense")
        print("2️⃣ View Expenses")
        print("3️⃣ Total Expense")
        print("4️⃣ Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expense()
        elif choice == '4':
            print("👋 Exiting... Have a great day!")
            break
        else:
            print("❌ Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
