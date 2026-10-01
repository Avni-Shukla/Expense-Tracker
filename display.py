def show_menu():
    print("\n" + "=" * 45)
    print("      PERSONAL EXPENSE TRACKER")
    print("=" * 45)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. View Category-wise Expense")
    print("5. View Unique Categories")
    print("6. Search Expense by Category")
    print("7. View Highest Expense Category")
    print("8. Exit")
    print("=" * 45)


def display_expenses(expenses):
    if len(expenses) == 0:
        print("\nNo expenses available.")
        return

    print("\n" + "-" * 80)
    print(f"{'ID':<5}{'Amount':<12}{'Category':<15}{'Date':<15}{'Note'}")
    print("-" * 80)

    for expense in expenses:
        print(
            f"{expense['id']:<5}"
            f"{expense['amount']:<12.2f}"
            f"{expense['category']:<15}"
            f"{expense['date']:<15}"
            f"{expense['note']}"
        )

    print("-" * 80)


def display_total_expense(total):
    print(f"\nTotal Expense: Rs. {total:.2f}")


def display_category_totals(category_totals):
    if len(category_totals) == 0:
        print("\nNo expenses available.")
        return

    print("\nCategory-wise Expense")
    print("-" * 35)
    print(f"{'Category':<20}{'Amount'}")
    print("-" * 35)

    for category, amount in category_totals.items():
        print(f"{category:<20}Rs. {amount:.2f}")

    print("-" * 35)


def display_categories(categories):
    if len(categories) == 0:
        print("\nNo categories available.")
        return

    print("\nUnique Expense Categories:")

    for category in sorted(categories):
        print("-", category)


def display_highest_category(category, amount):
    if category is None:
        print("\nNo expenses available.")
    else:
        print("\nHighest Expense Category")
        print(f"Category: {category}")
        print(f"Amount: Rs. {amount:.2f}")


def read_positive_amount():
    while True:
        try:
            amount = float(input("Enter amount: Rs. "))

            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                return amount

        except ValueError:
            print("Please enter a valid numeric amount.")


def read_non_empty_input(message):
    while True:
        value = input(message).strip()

        if value != "":
            return value

        print("This field cannot be empty.")