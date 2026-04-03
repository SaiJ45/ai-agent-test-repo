import sqlite3

def connect():
    return sqlite3.connect("test.db")

def crud_helper(query, params=None):
    if not isinstance(query, str):
        raise TypeError("Query must be a string")
    if params is not None and not isinstance(params, (list, tuple)):
        raise TypeError("Params must be a list or tuple")

    conn = connect()
    cursor = conn.cursor()

    try:
        if params is not None:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        if query.lstrip().upper().startswith("SELECT"):
            result = cursor.fetchall()
            conn.commit()
            return result
        else:
            conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        raise ValueError(f"Database error: {e}")
    finally:
        conn.close()

def get_user(user_id):
    if not isinstance(user_id, int) and user_id is not None:
        raise TypeError("User ID must be an integer or None")
    if user_id is None:
        return None
    if user_id == 0:
        return None
    query = "SELECT * FROM users WHERE id = ?"
    result = crud_helper(query, (user_id,))
    if result:
        return result[0]
    else:
        return None