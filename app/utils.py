def calculate_total(items):
    total = 0
    for i in items:
        total += i["price"] * i["quantity"]

    return total


def format_user(name, age):
    return f"Name: {name}, Age: {age}"  # type bug


def calculate_emi(principal, monthly_interest_rate, tenure_in_months):
    if not isinstance(principal, (int, float)) or not isinstance(monthly_interest_rate, (int, float)) or not isinstance(tenure_in_months, int):
        raise TypeError("Invalid input type. Principal and monthly interest rate must be numeric, and tenure in months must be an integer.")
    if principal <= 0 or monthly_interest_rate < 0 or tenure_in_months <= 0:
        raise ValueError("Invalid input value. Principal, monthly interest rate, and tenure in months must be positive.")
    try:
        emi = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** tenure_in_months / ((1 + monthly_interest_rate) ** tenure_in_months - 1)
        return emi
    except ZeroDivisionError:
        raise ValueError("Invalid input value. Monthly interest rate cannot be zero.")