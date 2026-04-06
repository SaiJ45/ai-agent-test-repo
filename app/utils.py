def calculate_total(items):
    total = 0
    for i in items:
        total += i["price"] * i["quantity"]

    return total


def format_user(name, age):
    return f"Name: {name}, Age: {age}"  # type bug

def calculate_emi(principal, monthly_interest_rate, tenure):
    if principal <= 0 or monthly_interest_rate <= 0 or tenure <= 0:
        raise ValueError("All input values must be greater than zero")
    emi = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** tenure) / ((1 + monthly_interest_rate) ** tenure - 1)
    return emi