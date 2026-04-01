from app.utils import calculate_total

def process_order(items):
    return calculate_total(items)


def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print(process_order([{"price": 10, "quantity": 2}]))