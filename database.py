import sqlite3
from bcrypt import hashpw, gensalt, checkpw

# Initialize the database
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Create users table with new fields
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        height REAL,
        weight REAL,
        age INTEGER,
        sex TEXT,
        health_conditions TEXT,
        smoking_status BOOLEAN,
        alcohol_consumption BOOLEAN
    )
    ''')

    # Create chat_history table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS chat_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        message TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (username) REFERENCES users (username)
    )
    ''')

    conn.commit()
    conn.close()

def register_user(name, username, password, height, weight, age, sex, health_conditions, smoking_status, alcohol_consumption):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    hashed_password = hashpw(password.encode(), gensalt())  # Hash the password
    try:
        cursor.execute('''
            INSERT INTO users (name, username, password, height, weight, age, sex, health_conditions, smoking_status, alcohol_consumption)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, username, hashed_password, height, weight, age, sex, health_conditions, smoking_status, alcohol_consumption))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def authenticate_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    if user and checkpw(password.encode(), user[0]):
        return True
    return False

def save_chat_history(username, message):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO chat_history (username, message) VALUES (?, ?)', (username, message))
    conn.commit()
    conn.close()

def get_chat_history(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT message, timestamp FROM chat_history WHERE username = ? ORDER BY timestamp', (username,))
    history = cursor.fetchall()
    conn.close()
    return history

# Initialize DB when this script is first run
init_db()
