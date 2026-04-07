def calculate_total(items):
    total = 0
    for i in items:
        total += i["price"] * i["quantity"]

    return total


def format_user(name, age):
    return f"Name: {name}, Age: {age}"  # type bug


def calculate_emi(principal, monthly_interest_rate, tenure):
    try:
        if not isinstance(principal, (int, float)) or not isinstance(monthly_interest_rate, (int, float)) or not isinstance(tenure, int):
            raise TypeError("Invalid input types. 'principal' and 'monthly_interest_rate' must be numbers and 'tenure' must be an integer.")
        if principal < 0 or monthly_interest_rate < 0 or tenure < 0:
            raise ValueError("Invalid input values. 'principal', 'monthly_interest_rate', and 'tenure' must be non-negative.")
        if tenure == 0:
            raise ZeroDivisionError("Tenure cannot be zero.")
        if abs(principal) > 1e308 or abs(monthly_interest_rate) > 1e308:
            raise OverflowError("Values are too large.")
        monthly_interest_rate = monthly_interest_rate / 100  # convert to decimal
        emi = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** tenure / ((1 + monthly_interest_rate) ** tenure - 1)
        return emi
    except (ZeroDivisionError, TypeError, ValueError, OverflowError) as e:
        raise Exception(f"Error calculating emi: {e}")