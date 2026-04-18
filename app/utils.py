def calculate_total(items):
    total = 0
    for i in items:
        total += i["price"] * i["quantity"]

    return total


def format_user(name, age):
    return f"Name: {name}, Age: {age}"  # type bug


def calculate_brokerage(total_cost, brokerage_rate):
    if not isinstance(total_cost, (int, float)) or not isinstance(brokerage_rate, (int, float)):
        raise TypeError("Both 'total_cost' and 'brokerage_rate' must be numbers.")
    if total_cost < 0 or brokerage_rate < 0:
        raise ValueError("Both 'total_cost' and 'brokerage_rate' must be non-negative.")
    if abs(total_cost) > 1e308 or abs(brokerage_rate) > 1e308:
        raise OverflowError("Values are too large.")
    return total_cost * brokerage_rate