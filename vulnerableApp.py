import sqlite3
import os

# 漏洞 1: SQL Injection (CWE-89)
def get_user_info(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # 【危險】直接將使用者輸入拼接進 SQL 語法中
    # Autofix 預期行為：會建議你改用參數化查詢 (Parameterized Query)，例如使用 ? 佔位符
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    
    result = cursor.fetchall()
    conn.close()
    return result

# 漏洞 2: Command Injection (CWE-78)
def ping_server(ip_address):
    # 【危險】直接將使用者輸入丟給系統 Shell 執行
    # Autofix 預期行為：會建議你改用 subprocess 模組，並將 shell=False
    command = "ping -c 1 " + ip_address
    os.system(command)

if __name__ == "__main__":
    # 模擬外部惡意輸入
    get_user_info("admin' OR '1'='1")
    ping_server("8.8.8.8; rm -rf /")