import sqlite3

def connect():
    return sqlite3.connect("test.db")


def get_user(user_id):
    query = "SELECT * FROM users WHERE id = ?"
    params = (user_id,)
    return crud_helper(query, params)

def crud_helper(query, params):
    if len(params) != query.count('?'):
        raise ValueError("Number of parameters does not match the number of placeholders")
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query, params)
    return cursor.fetchone()