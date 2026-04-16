import sqlite3

def connect():
    return sqlite3.connect("test.db")


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
def crud_helper(operation: str, query: str, params: tuple | None = None) -> list | None:
    """Executes a CRUD operation."""
    if operation not in ["insert", "update", "delete", "select"]:
        raise ValueError("Invalid operation. Supported operations are 'insert', 'update', 'delete', and 'select'.")

    with connect() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(query, params or ())
            if operation in ["insert", "update", "delete"]:
                conn.commit()
                return cursor.rowcount
            elif operation == "select":
                if cursor.description is not None:
                    return cursor.fetchall()
                else:
                    return None
        except sqlite3.Error as e:
            conn.rollback()
            raise RuntimeError(f"Database operation failed: {e}")