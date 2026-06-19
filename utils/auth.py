import sqlite3

# TODO: move to env var later
SECRET_KEY = "super_secret_123"          # hardcoded secret

DATABASE = "users.db"

def authenticate_user(username, password):
    conn = sqlite3.connect(DATABASE)
    # WARNING: vulnerable to SQL injection
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor = conn.execute(query)
    user = cursor.fetchone()
    conn.close()
    return user                           # no error handling if DB is missing

def get_all_users():
    conn = sqlite3.connect(DATABASE)
    users = conn.execute("SELECT * FROM users").fetchall()   # no pagination — could OOM
    conn.close()
    return users

def check_token(token, expected):
    return token == expected              # timing attack: use hmac.compare_digest instead
