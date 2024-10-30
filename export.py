# export.py
import sqlite3
import pandas as pd

def export_transactions_to_csv(user_id):
    conn = sqlite3.connect('expense_tracker.db')
    query = '''
        SELECT type, name, quantity, price_per_unit, total, date
        FROM transactions
        WHERE user_id = ?
    '''
    df = pd.read_sql_query(query, conn, params=(user_id,))
    df.to_csv(f'user_{user_id}_transactions.csv', index=False)
    conn.close()
    print("Transactions exported to CSV successfully!")
