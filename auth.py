# auth.py
import sqlite3
import bcrypt

def register_user(username, password, confirm_password, phone_number, job_title):
    # Check if passwords match
    if password != confirm_password:
        return False, "Passwords do not match!"

    # Additional validation can be added here (e.g., validate phone number)

    conn = sqlite3.connect('expense_tracker.db')
    cursor = conn.cursor()

    # Check if username already exists
    cursor.execute('SELECT username FROM users WHERE username = ?', (username,))
    if cursor.fetchone():
        conn.close()
        return False, "Username already exists!"

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Insert the new user into the database
    cursor.execute('''
        INSERT INTO users (username, password, phone_number, job_title)
        VALUES (?, ?, ?, ?)
    ''', (username, hashed_password, phone_number, job_title))
    conn.commit()
    conn.close()
    return True, "User registered successfully!"

def login_user(username, password):
    conn = sqlite3.connect('expense_tracker.db')
    cursor = conn.cursor()

    # Retrieve user data
    cursor.execute('SELECT user_id, password, phone_number, job_title FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()
    conn.close()

    if result:
        user_id, hashed_password, phone_number, job_title = result
        # Check if the provided password matches the hashed password
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            user_data = {
                'user_id': user_id,
                'phone_number': phone_number,
                'job_title': job_title
            }
            return True, user_data  # Login successful
        else:
            return False, "Invalid password!"
    else:
        return False, "Username not found!"
