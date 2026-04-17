import logging

def calculate_total(items):
    total = 0
    for i in items:
        total += i["price"] * i["quantity"]

    return total


def format_user(name, age):
    return f"Name: {name}, Age: {age}"  # type bug


def calculate_brokerage(total_value):
    try:
        if total_value is None:
            raise TypeError("Total value cannot be None.")
        if not isinstance(total_value, (int, float)):
            raise TypeError("Total value must be a number.")
        if total_value < 0:
            raise ValueError("Total value must be non-negative.")
        if abs(total_value) > 1e308:
            raise OverflowError("Total value is too large.")
        if total_value == 0:
            brokerage = 0  # fixed brokerage for zero total value
        else:
            brokerage_percentage = 0.05  # assuming 5% brokerage
            brokerage = total_value * brokerage_percentage
        return {"decision": "success", "brokerage": brokerage}
    except (TypeError, ValueError, OverflowError) as e:
        logging.error(f"Error calculating brokerage: {e}")
        return {"decision": "failure", "error": str(e)}