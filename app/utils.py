import logging

def calculate_total(items):
    total = 0
    for i in items:
        total += i["price"] * i["quantity"]

    return total


def format_user(name, age):
    return f"Name: {name}, Age: {age}"  # type bug


def calculate_brokerage(total_order_value, brokerage_rate, other_fees=0):
    if not isinstance(total_order_value, (int, float)) or not isinstance(brokerage_rate, (int, float)) or not isinstance(other_fees, (int, float)):
        raise TypeError("All inputs must be numbers.")
    if total_order_value < 0 or brokerage_rate < 0 or other_fees < 0:
        raise ValueError("All inputs must be non-negative.")
    if abs(total_order_value) > 1e308 or abs(brokerage_rate) > 1e308 or abs(other_fees) > 1e308:
        raise OverflowError("Values are too large.")
    if brokerage_rate == 0:
        return other_fees
    try:
        brokerage = (total_order_value * brokerage_rate) / 100 + other_fees
        return brokerage
    except Exception as e:
        logging.error(f"Error calculating brokerage: {e}")
        return None