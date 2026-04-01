import logging
from app.utils import calculate_total

def process_order(items):
    if not items:
        return 0

    total = 0
    for item in items:
        try:
            if not isinstance(item, dict) or "price" not in item or "quantity" not in item:
                raise ValueError("Invalid item format. Each item must be a dictionary with 'price' and 'quantity' keys.")
            if not isinstance(item["price"], (int, float)) or not isinstance(item["quantity"], int):
                raise TypeError("Invalid item values. 'price' must be a number and 'quantity' must be an integer.")
            if item["price"] < 0 or item["quantity"] < 0:
                raise ValueError("Invalid item values. 'price' and 'quantity' must be non-negative.")
            total += item["price"] * item["quantity"]
        except (ValueError, TypeError) as e:
            logging.error(f"Error processing item: {e}")
    return total


def divide(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both 'a' and 'b' must be numbers.")
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        if a < 0 or b < 0:
            raise ValueError("Both 'a' and 'b' must be non-negative.")
        if abs(a) > 1e308 or abs(b) > 1e308:
            raise OverflowError("Values are too large.")
        return a / b
    except (ZeroDivisionError, TypeError, ValueError, OverflowError) as e:
        logging.error(f"Error dividing: {e}")
        return None


if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    print(process_order([{"price": 10, "quantity": 2}]))