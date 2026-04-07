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
def crud_helper(query: str, params: tuple | None = None, query_type: str = "select") -> list | int | None:
    """Executes a CRUD operation."""
    if not isinstance(query, str) or not query.strip():
        raise ValueError("Query must be a non-empty string.")
    if not isinstance(query_type, str) or not query_type.strip():
        raise ValueError("Query type must be a non-empty string.")
    if query_type not in ["insert", "update", "delete", "select"]:
        raise ValueError("Invalid query type. Must be 'insert', 'update', 'delete', or 'select'.")
    if params is not None and not isinstance(params, tuple):
        raise TypeError("Params must be a tuple or None.")

    if params is None:
        params = ()
    elif len(params) == 0:
        raise ValueError("Params cannot be an empty tuple.")

    with connect() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(query, params)
            if query_type == "insert":
                return cursor.lastrowid
            elif query_type in ["update", "delete"]:
                return cursor.rowcount
            elif cursor.description is not None:
                return cursor.fetchall()
            conn.commit()
        except sqlite3.Error as e:
            conn.rollback()
            raise RuntimeError(f"Database operation failed: {e}")