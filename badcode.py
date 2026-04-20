import sqlite3

def login(username, password):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    # 這是要在這個 PR 裡新增的危險代碼
    query = f"SELECT * FROM users WHERE user='{username}' AND pass='{password}'"
    cursor.execute(query)
    return cursor.fetchall()