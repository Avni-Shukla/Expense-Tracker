def calculate_total_expense(expenses):
    """
    Returns the total amount of all expenses.
    """
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    return total


def calculate_category_totals(expenses):
    """
    Returns a dictionary containing category-wise total expenses.
    """
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] = category_totals[category] + amount
        else:
            category_totals[category] = amount

    return category_totals


def get_highest_expense_category(expenses):
    """
    Returns the category with the highest total expense.
    """
    category_totals = calculate_category_totals(expenses)

    if len(category_totals) == 0:
        return None, 0

    highest_category = ""
    highest_amount = 0

    for category, amount in category_totals.items():
        if amount > highest_amount:
            highest_category = category
            highest_amount = amount

    return highest_category, highest_amount