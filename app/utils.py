def calculate_total(items):
    total = 0
    for i in items:
        total += i["price"] * i["quantity"]

    return total


def calculate_brokerage(items):
    total = calculate_total(items)
    brokerage = total * 0.001  # 0.1% of the transaction amount
    return brokerage


def format_user(name, age):
    return f"Name: {name}, Age: {age}"  # type bug