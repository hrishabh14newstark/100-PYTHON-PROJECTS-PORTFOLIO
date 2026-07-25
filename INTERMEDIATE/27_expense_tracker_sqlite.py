"""
27: Expense Tracker
Implement CRUD operations with SQLite.
"""
import sqlite3

def init_db():
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, item TEXT, cost REAL)")
    conn.commit()
    conn.close()

def add_expense(item, cost):
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO expenses (item, cost) VALUES (?, ?)", (item, cost))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    add_expense("Coffee", 4.50)
    print("Expense added to SQLite DB.")
