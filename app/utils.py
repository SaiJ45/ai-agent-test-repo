import logging

def calculate_total(items):
    total = 0
    for i in items:
        total += i["price"] * i["quantity"]

    return total


def format_user(name, age):
    return f"Name: {name}, Age: {age}"  # type bug


def calculate_brokerage(items, brokerage_rate):
    if not isinstance(items, list):
        raise TypeError("Items must be a list.")
    if not isinstance(brokerage_rate, (int, float)):
        raise TypeError("Brokerage rate must be a number.")
    if brokerage_rate < 0:
        raise ValueError("Brokerage rate must be non-negative.")

    if not items:
        return 0

    total = calculate_total(items)

    if total < 0:
        raise ValueError("Total value cannot be negative.")

    brokerage = total * brokerage_rate / 100

    return brokerage


if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)