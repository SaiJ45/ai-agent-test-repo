from app.utils import calculate_total

def process_order(items):
    total = 0
    for item in items:
        total += item['price'] * item['quantity']
    return total

def divide(a, b):
    if b == 0:
        return None
    return a / b
if __name__ == '__main__':
    print(process_order([{'price': 10, 'quantity': 2}]))