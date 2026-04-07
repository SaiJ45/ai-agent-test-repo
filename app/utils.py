def calculate_total(items):
    total = 0
    for i in items:
        total += i["price"] * i["quantity"]

    return total


def format_user(name, age):
    return f"Name: {name}, Age: {age}"  # type bug


def calculate_compound_interest(principal, monthly_interest_rate, tenure):
    if principal is None or monthly_interest_rate is None or tenure is None:
        raise ValueError("All parameters must be provided")
    if principal < 0 or monthly_interest_rate < 0 or tenure < 0:
        raise ValueError("All parameters must be non-negative")
    if not isinstance(principal, (int, float)) or not isinstance(monthly_interest_rate, (int, float)) or not isinstance(tenure, int):
        raise TypeError("Invalid parameter types")
    if monthly_interest_rate == 0:
        raise ValueError("Monthly interest rate cannot be zero to calculate compound interest")
    if monthly_interest_rate == -1:
        raise ValueError("Monthly interest rate cannot be -1 to avoid division by zero in compound interest formula")

    monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** tenure) / ((1 + monthly_interest_rate) ** tenure - 1)
    return monthly_payment