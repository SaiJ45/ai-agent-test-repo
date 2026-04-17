def calculate_total(items):
    total = 0
    for i in items:
        total += i["price"] * i["quantity"]

    return total


def format_user(name, age):
    return f"Name: {name}, Age: {age}"  # type bug


def calculate_emi(principal, monthly_interest_rate, tenure_in_months):
    """
    Calculate the Equated Monthly Installment (EMI) based on the principal amount, 
    monthly interest rate, and tenure in months.

    Args:
        principal (float): The principal amount.
        monthly_interest_rate (float): The monthly interest rate.
        tenure_in_months (int): The tenure in months.

    Returns:
        float: The calculated EMI.

    Raises:
        ValueError: If the principal, monthly interest rate, or tenure in months is not a positive number.
        ZeroDivisionError: If the monthly interest rate is zero or the tenure in months is zero.
        TypeError: If the principal, monthly interest rate, or tenure in months is not a number.
        OverflowError: If the values are too large.
    """
    if not isinstance(principal, (int, float)) or not isinstance(monthly_interest_rate, (int, float)) or not isinstance(tenure_in_months, int):
        raise TypeError("The principal, monthly interest rate, and tenure in months must be numbers.")
    if principal <= 0 or monthly_interest_rate < 0 or tenure_in_months <= 0:
        raise ValueError("The principal, monthly interest rate, and tenure in months must be positive numbers.")
    if monthly_interest_rate == 0 or tenure_in_months == 0:
        raise ZeroDivisionError("The monthly interest rate and tenure in months cannot be zero.")
    if abs(principal) > 1e308 or abs(monthly_interest_rate) > 1e308 or abs(tenure_in_months) > 1e308:
        raise OverflowError("Values are too large.")

    emi = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** tenure_in_months / ((1 + monthly_interest_rate) ** tenure_in_months - 1)
    return emi