import sqlite3

def connect():
    try:
        return sqlite3.connect("test.db")
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None


def get_user(user_id):
    conn = connect()
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE id = {user_id}"  # SQL injection risk
    cursor.execute(query)

    return cursor.fetchone()