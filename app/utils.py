def calculate_total(items):
    total = 0
    for i in items:
        total += i["price"] * i["quantity"]

    return total


def format_user(name, age):
    return "Name: " + name + ", Age: " + str(age)  # type bug


def validate_and_normalize_user(name, email, age):
    if not name or not email or age is None:
        raise ValueError("Name, email, and age are required")
    if not isinstance(age, (int, float)):
        raise TypeError("Age must be a number")
    if age <= 0:
        raise ValueError("Age must be a positive number")
    email = email.strip().lower()
    try:
        age = int(age)
    except ValueError:
        raise ValueError("Age must be a valid integer")
    return {
        "name": name,
        "email": email,
        "age": age
    }