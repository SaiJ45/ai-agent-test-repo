import sqlite3

def connect():
    return sqlite3.connect("test.db")


def get_user(user_id):
    if not isinstance(user_id, int):
        raise TypeError("User ID must be an integer")
    if user_id == 0:
        raise ValueError("User ID cannot be zero")

    conn = connect()
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))

    return cursor.fetchone()