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
def crud_helper(query: str, params: tuple | None = None) -> list | None:
    """Executes a CRUD operation."""
    with connect() as conn:
        cursor = conn.cursor()
        try:
            if query.lower().startswith("insert"):
                cursor.execute(query, params or ())
                conn.commit()
                return cursor.lastrowid
            elif query.lower().startswith("update"):
                cursor.execute(query, params or ())
                conn.commit()
                return cursor.rowcount
            elif query.lower().startswith("delete"):
                cursor.execute(query, params or ())
                conn.commit()
                return cursor.rowcount
            else:
                cursor.execute(query, params or ())
                if cursor.description is not None:
                    return cursor.fetchall()
                conn.commit()
        except sqlite3.Error as e:
            conn.rollback()
            raise RuntimeError(f"Database operation failed: {e}")