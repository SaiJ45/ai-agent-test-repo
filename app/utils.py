import logging

def calculate_total(items):
    total = 0
    for i in items:
        total += i["price"] * i["quantity"]

    return total


def format_user(name, age):
    return f"Name: {name}, Age: {age}"  # type bug


def calculate_brokerage(total_cost):
    if not isinstance(total_cost, (int, float)):
        raise TypeError("Total cost must be a number.")
    if total_cost < 0:
        raise ValueError("Total cost must be non-negative.")
    if total_cost == 0:
        return 0
    if abs(total_cost) > 1e308:
        raise OverflowError("Total cost is too large.")
    brokerage_percentage = 0.01  # assuming 1% brokerage
    brokerage = total_cost * brokerage_percentage
    return brokerage