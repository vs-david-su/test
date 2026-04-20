from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/user')
def get_user():
    # 明確的外部輸入來源 (Taint Source)
    username = request.args.get('username')
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # 危險的 SQL 拼接 (Taint Sink)
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    
    row = cursor.fetchone()
    conn.close()
    return str(row)