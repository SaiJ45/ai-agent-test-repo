from app.utils import calculate_total
import sqlite3

def get_user(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def process_order(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]

    total = calculate_total(items)

    return total


def divide(a, b):
    if b == 0:
        return None
    return a / b


if __name__ == "__main__":
    print(process_order([{"price": 10, "quantity": 2}]))