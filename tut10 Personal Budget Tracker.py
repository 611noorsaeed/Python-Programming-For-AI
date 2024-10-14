# Features:
# Main Menu (with loop and if-statements):
#
# Show options like Add Income, Add Expense, View Summary, and Exit.
# Add Income Function:
#
# Input income and categorize it (e.g., salary, freelance, etc.).
# Store income amounts in a dictionary with categories as keys.
# Add Expense Function:
#
# Input expense details (amount, description) and categorize it (e.g., groceries, utilities, entertainment).
# Store expenses in a dictionary and keep track of the total expenses in each category.
# View Summary Function:
#
# Display the total income, expenses, and balance.
# Show expenses broken down by category, and check if the user is overspending.


budget = {
    'income': {},
    'expenses': {}
}


def add_income(category, amount):
    if category in budget['income']:
        budget['income'][category] += amount
    else:
        budget['income'][category] = amount
    print(f"Added {amount} to {category} income.")


def add_expense(category, amount, description):
    if category in budget['expenses']:
        budget['expenses'][category].append({'amount': amount, 'description': description})
    else:
        budget['expenses'][category] = [{'amount': amount, 'description': description}]
    print(f"Added expense: {description}, amount: {amount} to {category}.")


def view_summary():
    total_income = sum(budget['income'].values())
    total_expenses = sum(sum(item['amount'] for item in expenses) for expenses in budget['expenses'].values())
    balance = total_income - total_expenses

    print("\n--- Budget Summary ---")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Balance: ${balance:.2f}")
    print("\n--- Expense Breakdown ---")
    for category, expenses in budget['expenses'].items():
        total_category_expenses = sum(item['amount'] for item in expenses)
        print(f"{category}: ${total_category_expenses:.2f}")

    if balance < 0:
        print("\nWarning: You are overspending!")
    else:
        print("\nYou're managing your budget well.")


while True:
    print("\n1. Add Income\n2. Add Expense\n3. View Summary\n4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        income_category = input("Enter income category (e.g., Salary, Freelance): ")
        amount = float(input("Enter income amount: "))
        add_income(income_category, amount)
    elif choice == 2:
        expense_category = input("Enter expense category (e.g., Groceries, Utilities, Entertainment): ")
        amount = float(input("Enter expense amount: "))
        description = input("Enter description of the expense: ")
        add_expense(expense_category, amount, description)
    elif choice == 3:
        view_summary()
    elif choice == 4:
        break
    else:
        print("Invalid choice. Try again.")
