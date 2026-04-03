import sqlite3

def connect():
    try:
        return sqlite3.connect("test.db")
    except sqlite3.Error as e:
        raise RuntimeError(f"Failed to connect to database: {e}")


def get_user(user_id):
    conn = connect()
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))

    return cursor.fetchone()