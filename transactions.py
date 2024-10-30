# transactions.py
import sqlite3
from datetime import datetime

def add_transaction(user_id, type, name, quantity, price_per_unit):
    conn = sqlite3.connect('expense_tracker.db')
    cursor = conn.cursor()
    total = quantity * price_per_unit
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
        INSERT INTO transactions (user_id, type, name, quantity, price_per_unit, total, date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (user_id, type, name, quantity, price_per_unit, total, date))
    conn.commit()
    conn.close()
    print(f"{type.capitalize()} added successfully!")
