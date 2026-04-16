def calculate_total(items):
    total = 0
    for i in items:
        total += i["price"] * i["quantity"]

    return total


def format_user(name, age):
    return f"Name: {name}, Age: {age}"  # type bug


def calculate_brokerage(transaction_amount, brokerage_rate):
    try:
        if transaction_amount is None or brokerage_rate is None:
            raise ValueError("Transaction amount and brokerage rate cannot be None.")
        if not isinstance(transaction_amount, (int, float)) or not isinstance(brokerage_rate, (int, float)):
            raise TypeError("Transaction amount and brokerage rate must be numbers.")
        if transaction_amount < 0 or brokerage_rate < 0:
            raise ValueError("Transaction amount and brokerage rate must be non-negative.")
        if abs(transaction_amount) > 1e308 or abs(brokerage_rate) > 1e308:
            raise OverflowError("Values are too large.")
        if brokerage_rate == 0:
            return 0
        return transaction_amount * (brokerage_rate / 100)
    except (ZeroDivisionError, TypeError, ValueError, OverflowError) as e:
        print(f"Error calculating brokerage: {e}")
        return None