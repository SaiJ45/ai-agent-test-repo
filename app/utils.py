import logging

def calculate_total(items):
    total = 0
    for i in items:
        total += i["price"] * i["quantity"]

    return total


def format_user(name, age):
    return f"Name: {name}, Age: {age}"  # type bug


def calculate_brokerage(total_cost, brokerage_percentage):
    if total_cost is None or brokerage_percentage is None:
        raise ValueError("Total cost and brokerage percentage cannot be None.")
    if not isinstance(total_cost, (int, float)) or not isinstance(brokerage_percentage, (int, float)):
        raise TypeError("Total cost and brokerage percentage must be numbers.")
    if total_cost < 0 or brokerage_percentage < 0:
        raise ValueError("Total cost and brokerage percentage must be non-negative.")
    if abs(total_cost) > 1e308 or abs(brokerage_percentage) > 1e308:
        raise OverflowError("Values are too large.")
    if brokerage_percentage == 0:
        return 0
    try:
        brokerage = total_cost * (brokerage_percentage / 100)
        return brokerage
    except Exception as e:
        logging.error(f"Error calculating brokerage: {e}")
        return None