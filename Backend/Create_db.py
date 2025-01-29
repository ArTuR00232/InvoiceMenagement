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

def tableMoney():
    conn = Connect.DB()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE "Money" (
	"iduser"	INTEGER NOT NULL,
	"Date"	    TEXT NOT NULL,
	"Spend"	    NUMERIC NOT NULL,
	"id"	    INTEGER NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
    );''')

    conn.commit()
    cursor.close()
    conn.close()

def tableBank():
    conn = Connect.DB()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE "Bank" (
	"iduser"	INTEGER NOT NULL,
	"DateM"	    TEXT NOT NULL,
	"SpendM"	NUMERIC NOT NULL,
	"id"	    INTEGER NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
    );''')
    conn.commit()
    cursor.close()
    conn.close()

def tableMarker():
    conn = Connect.DB()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE "marker" (
	"id"	INTEGER,
	"Name"	TEXT,
	"color"	TEXT,
	"idUser"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
    );
    ''')
    conn.commit()
    cursor.close()
    conn.close()



def init():
    createDB()
    tableUser()
    Tablecode()
    TableKey()
    tableMoney()
    tableBank()
    tableMarker()