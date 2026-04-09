import sqlite3

def connect():
    try:
        return sqlite3.connect("test.db")
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None


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