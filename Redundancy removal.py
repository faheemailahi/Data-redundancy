import sqlite3
import re

# Initialize SQLite DB
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    department TEXT
)
''')
conn.commit()

# Validate email format
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# Insert data only if valid and not duplicate
def add_user(name, email, department):
    if not is_valid_email(email):
        print("❌ Invalid email format.")
        return

    try:
        cursor.execute("INSERT INTO users (name, email, department) VALUES (?, ?, ?)", (name, email, department))
        conn.commit()
        print("✅ Data added successfully.")
    except sqlite3.IntegrityError:
        print("⚠️ Duplicate entry found. Data not inserted.")

# Show all users
def display_users():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# 🧪 Sample Testing
while True:
    print("\n1. Add User\n2. View Users\n3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        email = input("Enter email: ")
        department = input("Enter department: ")
        add_user(name, email, department)

    elif choice == "2":
        display_users()

    elif choice == "3":
        print("Bye! ✅")
        break

    else:
        print("❌ Invalid choice.")
