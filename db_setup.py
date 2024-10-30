# db_setup.py
import sqlite3

def create_user_table():
    conn = sqlite3.connect('expense_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            phone_number TEXT,
            job_title TEXT
        )
    ''')
    conn.commit()
    conn.close()

def create_expense_table():
    conn = sqlite3.connect('expense_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            type TEXT,
            name TEXT,
            quantity INTEGER,
            price_per_unit REAL,
            total REAL,
            date TEXT,
            FOREIGN KEY(user_id) REFERENCES users(user_id)
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_user_table()
    create_expense_table()
    print("Database initialized successfully.")
