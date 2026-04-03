import sqlite3

def connect():
    return sqlite3.connect("test.db")

def validate_input(data):
    if data is None:
        raise ValueError("Input data cannot be None")
    if not isinstance(data, dict):
        raise ValueError("Input data must be a dictionary")
    for key, value in data.items():
        if not isinstance(key, str):
            raise ValueError("Key must be a string")
        if not isinstance(value, (str, int, float)):
            raise ValueError("Value must be a string, integer, or float")

def crud_helper(query_type, table_name, data):
    conn = connect()
    cursor = conn.cursor()
    try:
        if query_type == "insert":
            columns = ", ".join(data.keys())
            placeholders = ", ".join(["?"] * len(data))
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            cursor.execute(query, list(data.values()))
        elif query_type == "update":
            set_statements = ", ".join([f"{key} = ?" for key in data.keys()])
            query = f"UPDATE {table_name} SET {set_statements} WHERE id = ?"
            cursor.execute(query, list(data.values()) + [data.get("id")])
        elif query_type == "delete":
            query = f"DELETE FROM {table_name} WHERE id = ?"
            cursor.execute(query, (data.get("id"),))
        elif query_type == "select":
            query = f"SELECT * FROM {table_name} WHERE id = ?"
            cursor.execute(query, (data.get("id"),))
            return cursor.fetchone()
        else:
            raise ValueError("Invalid query type")
        conn.commit()
    finally:
        conn.close()

def get_user(user_id):
    data = {"id": user_id}
    return crud_helper("select", "users", data)


def get_user(user_id):
    conn = connect()
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE id = {user_id}"  # SQL injection risk
    cursor.execute(query)

    return cursor.fetchone()