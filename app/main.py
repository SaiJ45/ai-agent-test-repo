from app.utils import calculate_total

def process_order(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]

    # duplicate logic (bad practice)
    total = calculate_total(items)

    return total


def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both a and b must be numbers")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    if a < 0 or b < 0:
        raise ValueError("Both a and b must be non-negative")
    return a / b


if __name__ == "__main__":
    print(process_order([{"price": 10, "quantity": 2}]))