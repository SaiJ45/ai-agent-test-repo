import sqlite3

def connect():
    return sqlite3.connect("test.db")


def get_user(user_id):
    if not isinstance(user_id, int) or user_id < 0:
        raise ValueError("Invalid user ID")

    conn = connect()
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))

    return cursor.fetchone()