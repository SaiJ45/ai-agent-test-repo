import logging

def calculate_total(items):
    total = 0
    for i in items:
        total += i["price"] * i["quantity"]

    return total


def format_user(name, age):
    return f"Name: {name}, Age: {age}"  # type bug


def calculate_brokerage(items, brokerage_rate, other_fees=0):
    if not isinstance(items, list) or not all(isinstance(item, dict) for item in items):
        raise TypeError("Items must be a list of dictionaries.")
    if not all("price" in item and "quantity" in item for item in items):
        raise ValueError("Each item must be a dictionary with 'price' and 'quantity' keys.")
    if not all(isinstance(item["price"], (int, float)) and isinstance(item["quantity"], int) for item in items):
        raise TypeError("Invalid item values. 'price' must be a number and 'quantity' must be an integer.")
    if not all(item["price"] >= 0 and item["quantity"] >= 0 for item in items):
        raise ValueError("Invalid item values. 'price' and 'quantity' must be non-negative.")
    if not isinstance(brokerage_rate, (int, float)) or not isinstance(other_fees, (int, float)):
        raise TypeError("Brokerage rate and other fees must be numbers.")
    if brokerage_rate < 0 or other_fees < 0:
        raise ValueError("Brokerage rate and other fees must be non-negative.")
    if abs(brokerage_rate) > 1e308 or abs(other_fees) > 1e308:
        raise OverflowError("Brokerage rate and other fees are too large.")
    try:
        if not items:
            raise ValueError("Items list cannot be empty.")
        total_order_value = calculate_total(items)
        if abs(total_order_value) > 1e308:
            raise OverflowError("Total order value is too large.")
        if brokerage_rate == 0:
            return other_fees
        if total_order_value == 0:
            return other_fees
        brokerage = (total_order_value * brokerage_rate) / 100 + other_fees
        return brokerage
    except (ZeroDivisionError, TypeError, ValueError, OverflowError) as e:
        logging.error(f"Error calculating brokerage: {e}")
        return None