def calculate_total(items):
    total = 0
    for i in items:
        total += i["price"] * i["quantity"]

    return total


def format_user(name, age):
    return f"Name: {name}, Age: {age}"  # type bug


def calculate_emi(principal, monthly_interest_rate, tenure):
    if principal is None or monthly_interest_rate is None or tenure is None:
        raise ValueError("All inputs must be numbers")
    if not isinstance(principal, (int, float)) or not isinstance(monthly_interest_rate, (int, float)) or not isinstance(tenure, int):
        raise TypeError("All inputs must be numbers")
    if principal < 0 or monthly_interest_rate < 0 or tenure <= 0:
        raise ValueError("Principal, monthly interest rate, and tenure must be positive numbers")
    if monthly_interest_rate == 0:
        return principal / tenure
    emi = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** tenure) / ((1 + monthly_interest_rate) ** tenure - 1)
    return emi