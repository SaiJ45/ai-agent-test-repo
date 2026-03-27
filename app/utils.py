# app/utils.py

def calculate_emi(principal, monthly_interest_rate, tenure_in_months):
    """
    Calculate the fixed monthly payment covering both interest and principal repayment.

    Args:
        principal (float): The initial amount borrowed.
        monthly_interest_rate (float): The monthly interest rate as a decimal.
        tenure_in_months (int): The loan tenure in months.

    Returns:
        float: The fixed monthly payment.
    """
    monthly_payment = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** tenure_in_months) / ((1 + monthly_interest_rate) ** tenure_in_months - 1)
    return round(monthly_payment, 2)


def calculate_total(items):
    """
    Calculate the total cost of items.

    Args:
        items (list): A list of dictionaries containing 'price' and 'quantity' keys.

    Returns:
        float: The total cost.
    """
    total = 0
    for i in items:
        total += i["price"] * i["quantity"]

    return total


def format_user(name, age):
    """
    Format a user's name and age.

    Args:
        name (str): The user's name.
        age (int): The user's age.

    Returns:
        str: A formatted string containing the user's name and age.
    """
    return f"Name: {name}, Age: {age}"