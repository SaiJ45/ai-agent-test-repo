def process_order(order):
    for item in order['items']:
        if 'price' not in item or 'quantity' not in item:
            raise ValueError("Order item is missing 'price' or 'quantity' field")
        if not isinstance(item['price'], (int, float)) or not isinstance(item['quantity'], int):
            raise ValueError("Order item 'price' must be a number and 'quantity' must be an integer")
        if item['price'] <= 0 or item['quantity'] <= 0:
            raise ValueError("Order item 'price' and 'quantity' must be greater than zero")
    # rest of the function remains the same