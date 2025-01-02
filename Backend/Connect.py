import sqlite3

def DB():
    conn = None
    try:
        conn = sqlite3.connect('bank.db')
    except sqlite3.Error as e:
        print(e)
    return conn