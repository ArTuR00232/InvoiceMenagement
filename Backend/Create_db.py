import Connect

def tableUser():
    #connect to an SQLite database(or create on if it doesn't exist)
    conn = Connect.DB()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE "Users" (
        "id" INTEGER NOR NULL UNIQUE,
        "username" TEXT NOT NULL,
        "password" TEXT NOT NULL,
        PRIMARY KEY("id" AUTOINCREMENT)
        );
        )
    ''')

def createDB():
    conn = Connect.DB()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE DATABASE "bank";
    ''')

def init():
    createDB()
    tableUser()