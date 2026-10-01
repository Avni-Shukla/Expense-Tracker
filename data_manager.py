def add_expense(expenses, amount, category, date, note):
    """
    Creates an expense dictionary and adds it to the expenses list.
    """

    if amount <= 0:
        return False, "Amount must be greater than zero."

    if category.strip() == "":
        return False, "Category cannot be empty."

    expense_id = len(expenses) + 1

    expense = {
        "id": expense_id,
        "amount": amount,
        "category": category.strip().title(),
        "date": date.strip(),
        "note": note.strip()
    }

    expenses.append(expense)

    return True, "Expense added successfully."


def get_all_expenses(expenses):
    """
    Returns the complete expense list.
    """
    return expenses