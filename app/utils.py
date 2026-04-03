def calculate_total(items):
    total = 0
    for i in items:
        total += i["price"] * i["quantity"]

    return total


def format_user(name, age):
    return f"Name: {name}, Age: {age}"

def calculate_emi(principal: float, monthly_interest_rate: float, tenure_in_months: int) -> float:
    """
    Calculate the Equated Monthly Installment (EMI) given the principal amount, 
    monthly interest rate, and tenure in months.

    Args:
    principal (float): The principal amount.
    monthly_interest_rate (float): The monthly interest rate.
    tenure_in_months (int): The tenure in months.

    Returns:
    float: The calculated EMI.
    """
    if not isinstance(principal, (int, float)) or not isinstance(monthly_interest_rate, (int, float)) or not isinstance(tenure_in_months, int):
        raise TypeError("All inputs must be numbers.")
    if principal < 0 or monthly_interest_rate < 0 or tenure_in_months <= 0:
        raise ValueError("All inputs must be positive or zero.")
    if monthly_interest_rate == 0:
        return principal / tenure_in_months
    emi = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** tenure_in_months) / ((1 + monthly_interest_rate) ** tenure_in_months - 1)
    return emi  # type bug