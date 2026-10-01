def get_unique_categories(expenses):
    """
    Uses a set to return unique expense categories.
    """
    categories = set()

    for expense in expenses:
        categories.add(expense["category"])

    return categories


def search_by_category(expenses, search_category):
    """
    Returns a list of expenses that match the entered category.
    """
    matched_expenses = []

    for expense in expenses:
        if expense["category"].lower() == search_category.strip().lower():
            matched_expenses.append(expense)

    return matched_expenses