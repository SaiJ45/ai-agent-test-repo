def calculate_total(items):
    total = 0
    for i in items:
        try:
            total += i["price"] * i["quantity"]
        except KeyError as e:
            raise ValueError(f"Invalid item: missing field '{e.args[0]}'") from e
        except TypeError:
            raise ValueError("Invalid item: 'price' or 'quantity' is not a number")

    return total


def format_user(name, age):
    return f"Name: {name}, Age: {age}"  # type bug