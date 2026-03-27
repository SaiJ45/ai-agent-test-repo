import sqlite3

def connect():
    return sqlite3.connect("test.db")


def get_user(user_id):
    conn = connect()
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE id = {user_id}"  # SQL injection risk
    cursor.execute(query)

    result = cursor.fetchone()
    if result is not None:
        # assuming the column that may cause division by zero error is the third column
        if result[2] == 0:
            return "Cannot divide by zero"
        else:
            # perform division here, replace 'result[1]' with the actual column you want to divide
            return result[1] / result[2]
    else:
        return None