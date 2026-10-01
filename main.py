import data_manager
import calculator
import expense_search as search
import display


def add_expense_flow(expenses):
    print("\n--- Add Expense ---")

    amount = display.read_positive_amount()
    category = display.read_non_empty_input("Enter category: ")
    date = display.read_non_empty_input("Enter date (DD-MM-YYYY): ")
    note = input("Enter note: ")

    success, message = data_manager.add_expense(
        expenses,
        amount,
        category,
        date,
        note
    )

    print(message)


def view_all_expenses_flow(expenses):
    print("\n--- All Expenses ---")

    all_expenses = data_manager.get_all_expenses(expenses)
    display.display_expenses(all_expenses)


def view_total_expense_flow(expenses):
    print("\n--- Total Expense ---")

    if len(expenses) == 0:
        print("No expenses available.")
        return

    total = calculator.calculate_total_expense(expenses)
    display.display_total_expense(total)


def view_category_wise_expense_flow(expenses):
    print("\n--- Category-wise Expense ---")

    category_totals = calculator.calculate_category_totals(expenses)
    display.display_category_totals(category_totals)


def view_unique_categories_flow(expenses):
    print("\n--- Unique Categories ---")

    categories = search.get_unique_categories(expenses)
    display.display_categories(categories)


def search_category_flow(expenses):
    print("\n--- Search Expense by Category ---")

    if len(expenses) == 0:
        print("No expenses available.")
        return

    category = display.read_non_empty_input("Enter category to search: ")
    matched_expenses = search.search_by_category(expenses, category)

    if len(matched_expenses) == 0:
        print("No expenses found in this category.")
    else:
        print(f"\nExpenses under category: {category.title()}")
        display.display_expenses(matched_expenses)


def view_highest_category_flow(expenses):
    print("\n--- Highest Expense Category ---")

    category, amount = calculator.get_highest_expense_category(expenses)
    display.display_highest_category(category, amount)


def main():
    expenses = []

    while True:
        display.show_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_expense_flow(expenses)

        elif choice == "2":
            view_all_expenses_flow(expenses)

        elif choice == "3":
            view_total_expense_flow(expenses)

        elif choice == "4":
            view_category_wise_expense_flow(expenses)

        elif choice == "5":
            view_unique_categories_flow(expenses)

        elif choice == "6":
            search_category_flow(expenses)

        elif choice == "7":
            view_highest_category_flow(expenses)

        elif choice == "8":
            print("\nThank you for using Personal Expense Tracker.")
            print("Program exited successfully.")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()