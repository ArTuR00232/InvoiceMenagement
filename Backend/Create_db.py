import Connect

def createDB():
    conn = Connect.DB()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE DATABASE "bank";
    ''')

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
def Tablecode():
    conn = Connect.DB()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE "RestorePassCode" (
                   "ID" INTEGER NOT NULL,
                   "IdUser" INTEGER NOT NULL,
                   "Code" TEXT,
                   PRIMARY KEY("ID" AUTOINCREMENT)
                   );''')
    conn.commit()
    cursor.close()
    conn.close()

def TableKey():
    conn = Connect.DB()
    cursor = conn.cursor()
    cursor.execute('''CRATE TABLE "KeyMaster" (
                   "ID" INTEGER NOT NULL,
                   "KEY" TEXT, 
                   PRIMARY KEY("ID" AUTOINCREMENT)
                   );''')
    conn.commit()
    cursor.close()
    conn.close()


def init():
    createDB()
    tableUser()
    Tablecode()
    TableKey()