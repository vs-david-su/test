import sqlite3
import os
import base64
    from Crypto.Cipher import AES

# 1. 絕對會中的 SQL Injection(CWE - 89)
# 規則：python.lang.security.database.sqlite - execute - string - format
def get_user(username):
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
    # Semgrep 最討厭這種 f - string 或 % 直接拼進 execute 的寫法
query = f"SELECT * FROM users WHERE username = '{username}'"
cursor.execute(query)
return cursor.fetchall()

# 2. 絕對會中的 Command Injection(CWE - 78)
# 規則：python.lang.security.audit.dangerous - os - system - audit
def run_ping(ip):
    # 直接把變數拼進系統指令，這對 Semgrep 來說是紅燈區
os.system("ping -c 1 " + ip)

# 3. 絕對會中的不安全評估(CWE - 95)
# 規則：python.lang.security.audit.dangerous - eval - usage
def risky_calc(user_data):
    # eval 是 Semgrep 的頭號通緝犯
return eval(user_data)

# 4. 絕對會中的硬編碼秘密(CWE - 798)
# 規則：python.lang.security.audit.hardcoded - password
DATABASE_PASSWORD = "super_secret_password_12345"

# 5. 絕對會中的不安全加密(CWE - 327)
# 規則：python.lang.security.audit.crypto - bad - cipher
def encrypt(data):
    # 使用 ECB 模式是加解密規則中的必殺項
cipher = AES.new("static_key_16byte", AES.MODE_ECB)
return cipher.encrypt(data)