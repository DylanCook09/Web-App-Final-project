import sqlite3

def get_db():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_entries_db():
    conn = sqlite3.connect('entries.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn_users = get_db()
    conn_users.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT
        )
    """)
    conn_users.commit()
    conn_users.close()

    conn_entries = get_entries_db()
    conn_entries.execute("""
        CREATE TABLE IF NOT EXISTS entries (
            created_on TEXT DEFAULT CURRENT_DATE PRIMARY KEY,
            mile_time INT,
            weight_lifted INT,
            calories_consumed INT
        )
    """)
    conn_entries.commit()
    conn_entries.close()

if __name__ == "__main__":
    init_db()
