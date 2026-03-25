from app.utils import calculate_total

def process_order(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]

    total = calculate_total(items)

    return total


def divide(a, b):
    if b == 0:
        return float('inf')
    return a / b


if __name__ == "__main__":
    print(process_order([{"price": 10, "quantity": 2}]))