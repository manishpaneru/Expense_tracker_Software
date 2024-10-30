# visualization.py
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def get_transactions_df(user_id):
    conn = sqlite3.connect('expense_tracker.db')
    df = pd.read_sql_query('''
        SELECT * FROM transactions WHERE user_id = ?
    ''', conn, params=(user_id,))
    conn.close()
    return df

def visualize_most_expenditure_item(user_id):
    df = get_transactions_df(user_id)
    expenses = df[df['type'] == 'expense']
    if not expenses.empty:
        item_totals = expenses.groupby('name')['total'].sum()
        item_totals.plot(kind='bar', title='Expenses by Item', ylabel='Total Spent ($)')
        plt.show()
    else:
        print("No expenses to display.")

def visualize_monthly_surplus(user_id):
    df = get_transactions_df(user_id)
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.to_period('M')
    monthly_data = df.groupby(['month', 'type'])['total'].sum().unstack().fillna(0)
    monthly_data['Surplus'] = monthly_data.get('earning', 0) - monthly_data.get('expense', 0)
    monthly_data['Surplus'].plot(kind='bar', title='Monthly Surplus', ylabel='Surplus ($)')
    plt.show()
