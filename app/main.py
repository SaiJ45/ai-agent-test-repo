from app.utils import calculate_total

def process_order(items):
    if not items:
        return 0
    total = 0
    for item in items:
        if not isinstance(item["price"], (int, float)) or not isinstance(item["quantity"], (int, float)):
            raise TypeError("Price and quantity must be numbers")
        if item["price"] < 0 or item["quantity"] < 0:
            raise ValueError("Price and quantity must be non-negative")
        total += item["price"] * item["quantity"]
    return total


def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print(process_order([{"price": 10, "quantity": 2}]))