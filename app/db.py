import sqlite3

def connect():
    return sqlite3.connect("test.db")


def get_user(user_id):
    conn = connect()
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))

    return cursor.fetchone()