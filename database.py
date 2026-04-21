import sqlite3

def get_db():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS users(
            username TEXT PRIMARY KEY,
            password TEXT
        );
        CREATE TABLE IF NOT EXISTS entries (
            created_on TEXT DEFAULT CURRENT_DATE PRIMARY KEY,
            mile_time INT,
            weight_lifted INT,
            calories_consumed INT
        );
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
