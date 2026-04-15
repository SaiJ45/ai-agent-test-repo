```python
import sqlite3

def connect():
    """Establish a connection to the SQLite database."""
    return sqlite3.connect("test.db")


def create_table(table_name, columns):
    """
    Create a table in the database.

    Args:
        table_name (str): The name of the table to create.
        columns (dict): A dictionary where keys are column names and values are data types.

    Returns:
        None
    """
    conn = connect()
    cursor = conn.cursor()

    column_definitions = ", ".join(f"{key} {value}" for key, value in columns.items())
    query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})"
    cursor.execute(query)
    conn.commit()


def insert_data(table_name, data):
    """
    Insert data into a table in the database.

    Args:
        table_name (str): The name of the table to insert data into.
        data (dict): A dictionary where keys are column names and values are the data to insert.

    Returns:
        None
    """
    conn = connect()
    cursor = conn.cursor()

    columns = ", ".join(data.keys())
    placeholders = ", ".join("?" for _ in data)
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    cursor.execute(query, list(data.values()))
    conn.commit()


def update_data(table_name, data, conditions):
    """
    Update data in a table in the database.

    Args:
        table_name (str): The name of the table to update data in.
        data (dict): A dictionary where keys are column names and values are the new data.
        conditions (dict): A dictionary where keys are column names and values are the conditions for the update.

    Returns:
        None
    """
    conn = connect()
    cursor = conn.cursor()

    set_statements = ", ".join(f"{key} = ?" for key in data)
    condition_statements = " AND ".join(f"{key} = ?" for key in conditions)
    query = f"UPDATE {table_name} SET {set_statements} WHERE {condition_statements}"
    cursor.execute(query, list(data.values()) + list(conditions.values()))
    conn.commit()


def delete_data(table_name, conditions):
    """
    Delete data from a table in the database.

    Args:
        table_name (str): The name of the table to delete data from.
        conditions (dict): A dictionary where keys are column names and values are the conditions for the deletion.

    Returns:
        None
    """
    conn = connect()
    cursor = conn.cursor()

    condition_statements = " AND ".join(f"{key} = ?" for key in conditions)
    query = f"DELETE FROM {table_name} WHERE {condition_statements}"
    cursor.execute(query, list(conditions.values()))
    conn.commit()


def get_user(user_id):
    """
    Retrieve a user from the database.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        tuple: The user data.
    """
    conn = connect()
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
    return cursor.fetchone()
```