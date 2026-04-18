import logging

def calculate_total(items):
    if not isinstance(items, list):
        raise TypeError("Items must be a list.")
    total = 0
    for i in items:
        if not isinstance(i, dict) or "price" not in i or "quantity" not in i:
            raise ValueError("Invalid item format. Each item must be a dictionary with 'price' and 'quantity' keys.")
        if not isinstance(i["price"], (int, float)) or not isinstance(i["quantity"], int):
            raise TypeError("Invalid item values. 'price' must be a number and 'quantity' must be an integer.")
        if i["price"] < 0 or i["quantity"] < 0:
            raise ValueError("Invalid item values. 'price' and 'quantity' must be non-negative.")
        total += i["price"] * i["quantity"]
    return total


def format_user(name, age):
    return f"Name: {name}, Age: {age}"  # type bug


def calculate_brokerage(items, brokerage_rate):
    if items is None or not isinstance(items, list):
        raise TypeError("Items must be a list.")
    if brokerage_rate is None or not isinstance(brokerage_rate, (int, float)):
        raise TypeError("Brokerage rate must be a number.")
    if brokerage_rate < 0:
        raise ValueError("Brokerage rate must be non-negative.")
    if abs(brokerage_rate) > 1e308:
        raise OverflowError("Brokerage rate is too large.")

    if not items:
        return 0

    total = calculate_total(items)

    if total < 0:
        raise ValueError("Total value cannot be negative.")
    if abs(total) > 1e308:
        raise OverflowError("Total value is too large.")

    if brokerage_rate == 0:
        return 0

    brokerage = total * brokerage_rate / 100

    return brokerage


if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)