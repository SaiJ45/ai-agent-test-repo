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
        if not isinstance(total_value, (int, float)):
            raise TypeError("Total value must be a number.")
        if total_value < 0:
            raise ValueError("Total value must be non-negative.")
        if total_value == 0:
            return 0
        if abs(total_value) > 1e308:
            raise OverflowError("Total value is too large.")
        brokerage_percentage = 0.05  # assuming 5% brokerage
        brokerage = total_value * brokerage_percentage
        return brokerage
    except (TypeError, ValueError, OverflowError) as e:
        logging.error(f"Error calculating brokerage: {e}")
        return None