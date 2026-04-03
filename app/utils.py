def calculate_emi(principal, monthly_interest_rate, tenure_in_months):
    if not isinstance(principal, (int, float)) or not isinstance(monthly_interest_rate, (int, float)) or not isinstance(tenure_in_months, int):
        raise TypeError("All inputs must be numbers")
    if principal is None or monthly_interest_rate is None or tenure_in_months is None:
        raise ValueError("None value is not allowed")
    if principal <= 0 or monthly_interest_rate <= 0 or tenure_in_months <= 0:
        raise ValueError("All inputs must be positive")
    if monthly_interest_rate == 0:
        return principal / tenure_in_months
    emi = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** tenure_in_months) / ((1 + monthly_interest_rate) ** tenure_in_months - 1)
    return emi


def calculate_total(items):
    total = 0
    for i in items:
        total += i["price"] * i["quantity"]

    return total


def format_user(name, age):
    return "Name: " + name + ", Age: " + str(age)