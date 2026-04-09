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


def get_user(user_id: int) -> tuple | None:
    """Fetches a user by ID."""
    if not isinstance(user_id, int):
        raise TypeError("User ID must be an integer.")
    
    query = "SELECT * FROM users WHERE id = ?"
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (user_id,))
        return cursor.fetchone()

# Adding a generic CRUD helper function
def crud_helper(query: str, params: tuple | None = None) -> list | None:
    """Executes a CRUD operation."""
    with connect() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(query, params or ())
            if cursor.description is not None:
                return cursor.fetchall()
            conn.commit()
        except sqlite3.Error as e:
            conn.rollback()
            raise RuntimeError(f"Database operation failed: {e}")