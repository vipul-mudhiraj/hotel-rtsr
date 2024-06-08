import sqlite3
from getpass import getpass

def sign_up():
    conn = sqlite3.connect('hotel_management.db')
    cursor = conn.cursor()
    
    username = input('Enter username: ')
    password = getpass('Enter password: ')
    
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()
    print('User registered successfully!')

def login():
    conn = sqlite3.connect('hotel_management.db')
    cursor = conn.cursor()
    
    username = input('Enter username: ')
    password = getpass('Enter password: ')
    
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    
    if user:
        print('Login successful!')
        return user[0]  # Return user_id
    else:
        print('Invalid username or password')
        return None

# Example usage
sign_up()
user_id = login()
if user_id:
    print(f'Logged in as user ID: {user_id}')
