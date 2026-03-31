def calculate_emi(principal, monthly_interest_rate, tenure_in_months):
    if not isinstance(principal, (int, float)) or not isinstance(monthly_interest_rate, (int, float)) or not isinstance(tenure_in_months, int):
        raise TypeError("Invalid input type. All inputs must be numbers.")
    if principal is None or monthly_interest_rate is None or tenure_in_months is None:
        raise ValueError("Input cannot be None.")
    if principal < 0 or monthly_interest_rate < 0 or tenure_in_months <= 0:
        raise ValueError("Invalid input value. Principal, monthly interest rate and tenure must be positive numbers.")
    if monthly_interest_rate == 0:
        raise ZeroDivisionError("Monthly interest rate cannot be zero.")
    if tenure_in_months == 0:
        raise ZeroDivisionError("Tenure in months cannot be zero.")

    emi = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** tenure_in_months / ((1 + monthly_interest_rate) ** tenure_in_months - 1)
    return emi


def calculate_total(items):
    total = 0
    for i in items:
        total += i["price"] * i["quantity"]

    return total


def format_user(name, age):
    if not isinstance(name, str):
        raise TypeError("Name must be a string.")
    if not isinstance(age, int):
        raise TypeError("Age must be an integer.")
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return "Name: " + name + ", Age: " + str(age)