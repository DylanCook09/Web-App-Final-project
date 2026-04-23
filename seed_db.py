#!/usr/bin/env python3
# Seed the database with sample data.
# Run this script once with: python seed_db.py
# Once you have seeded your data, you can run sqlite3 users.db in the terminal
# This opens a sqlite3 shell and you can run commands like:
# - .tables to see all tables
# - SELECT * FROM users; to see all users
# - .exit to exit the shell
# *Note: If you try to seed data and get an error about "UNIQUE constraint failed: users.username",
# it means you have already seeded the database.
# If you need to seed the database again, simply delete the users.db file and run the seed script again.

from database import get_db, init_db
import bcrypt

def seed_database():
    """Add sample users and fitness entries to the databases"""
    init_db()  # Ensure tables are created

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
        for date, mile_time, weight, calories in sample_entries:
            conn.execute(
                "INSERT INTO entries (created_on, mile_time, weight_lifted, calories_consumed) VALUES (?, ?, ?, ?)",
                (date, mile_time, weight, calories)
            )
            print("you did it")
        conn.commit()
    except Exception as e:
        print(f"Error seeding users: {e}")
        conn.rollback()
    finally:
        conn.close()

    print("\nDatabase seeding complete!")

if __name__ == "__main__":
    seed_database()
