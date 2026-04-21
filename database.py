import sqlite3

def get_db():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()

    conn.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT
        );
        
        CREATE TABLE IF NOT EXISTS user (
            weight_lifted INTEGER,
            reps INTEGER,
            mile_time TEXT
        );
    """)
    conn.commit()
    conn.close()

init_db()
