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
def crud_helper(query: str, params: tuple | None = None) -> int | list | None:
    """Executes a CRUD operation and returns the result."""
    with connect() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(query, params or ())
            if cursor.description is not None:
                result = cursor.fetchall()
            else:
                result = cursor.rowcount if query.lower().startswith("insert") else cursor.lastrowid
            conn.commit()
            return result
        except sqlite3.Error as e:
            conn.rollback()
            raise RuntimeError(f"Database operation failed: {e}")