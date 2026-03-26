import sqlite3

def connect():
    return sqlite3.connect('test.db')

def get_user(user_id):
    conn = connect()
    cursor = conn.cursor()
    query = f'SELECT * FROM users WHERE id = {user_id}'
    cursor.execute(query)
    return cursor.fetchone()