def calculate_total(items):
    total = 0
    for i in items:
        total += i["price"] * i["quantity"]

    return total


def format_user(name: str, age: int | str | None) -> str:
    if age is None:
        age = "Unknown"
    elif isinstance(age, int):
        age = str(age)
    elif not isinstance(age, str):
        raise TypeError("Age must be an integer or a string.")
    
    return f"Name: {name}, Age: {age}"