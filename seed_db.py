#!/usr/bin/env python3
# Seed the database with sample data.
# Run this script once with: python seed_db.py
# After running, you can open the database with:
# sqlite3 users.db
# Then use:
# .tables
# SELECT * FROM users;
# SELECT * FROM entries;
# .exit
# If you get a UNIQUE constraint error, delete users.db and run again.

from database import get_db, init_db
import bcrypt

def seed_database():
    """Add sample users and fitness entries to the database"""

    init_db()

    conn = get_db()

    sample_users = [
        ("alice", "Password123!"),
        ("bob", "SecurePass456@"),
        ("charlie", "MyPassword789#"),
    ]

    sample_entries = [
        ("2023-10-01", 480, 150, 2100),
        ("2023-10-02", 475, 155, 2050),
        ("2023-10-03", 490, 160, 2200),
    ]

    try:
        for username, password in sample_users:
            hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

            conn.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_pw)
            )

        print("Users seeded successfully.")

        for date, mile_time, weight, calories in sample_entries:
            conn.execute(
                "INSERT INTO entries (created_on, mile_time, weight_lifted, calories_consumed) VALUES (?, ?, ?, ?)",
                (date, mile_time, weight, calories)
            )

        print("Entries seeded successfully.")

        conn.commit()

    except Exception as e:
        print(f"Error seeding database: {e}")
        conn.rollback()

    finally:
        conn.close()

    print("Database seeding complete!")

if __name__ == "__main__":
    seed_database()