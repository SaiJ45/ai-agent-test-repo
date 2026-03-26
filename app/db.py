import sqlite3

def connect():
    return sqlite3.connect('test.db')

def get_user(user_id):
    return None