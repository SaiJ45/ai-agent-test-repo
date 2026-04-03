import sqlite3

def connect():
    return sqlite3.connect("test.db")


def get_user(user_id):
    if not isinstance(user_id, int) or user_id < 0:
        raise ValueError("User ID must be a non-negative integer")

    query = "SELECT * FROM users WHERE id = ?"
    return crud_helper(query, (user_id,))

def crud_helper(query, params=None):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute(query, params or ())
        if cursor.description is not None:
            return cursor.fetchall()
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        raise RuntimeError(f"Database error: {e}")
    finally:
        conn.close()

def create_user(name, email):
    if not isinstance(name, str) or not isinstance(email, str):
        raise ValueError("Name and email must be strings")
    if not name or not email:
        raise ValueError("Name and email cannot be empty")

    query = "INSERT INTO users (name, email) VALUES (?, ?)"
    crud_helper(query, (name, email))

def update_user(user_id, name, email):
    if not isinstance(user_id, int) or user_id < 0:
        raise ValueError("User ID must be a non-negative integer")
    if not isinstance(name, str) or not isinstance(email, str):
        raise ValueError("Name and email must be strings")
    if not name or not email:
        raise ValueError("Name and email cannot be empty")

    query = "UPDATE users SET name = ?, email = ? WHERE id = ?"
    crud_helper(query, (name, email, user_id))

def delete_user(user_id):
    if not isinstance(user_id, int) or user_id < 0:
        raise ValueError("User ID must be a non-negative integer")

    query = "DELETE FROM users WHERE id = ?"
    crud_helper(query, (user_id,))