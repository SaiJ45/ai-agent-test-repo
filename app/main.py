from app.utils import calculate_total

def process_order(items):
    if not items:
        return 0

    total = 0
    for item in items:
        if not isinstance(item, dict) or "price" not in item or "quantity" not in item:
            raise ValueError("Invalid item format. Each item must be a dictionary with 'price' and 'quantity' keys.")
        if not isinstance(item["price"], (int, float)) or not isinstance(item["quantity"], int):
            raise TypeError("Invalid item values. 'price' must be a number and 'quantity' must be an integer.")
        if item["price"] < 0 or item["quantity"] < 0:
            raise ValueError("Invalid item values. 'price' and 'quantity' must be non-negative.")
        total += item["price"] * item["quantity"]

    return total


def divide(a, b):
    if b == 0:
        return None
    return a / b


if __name__ == "__main__":
    print(process_order([{"price": 10, "quantity": 2}]))