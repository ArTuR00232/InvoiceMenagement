from cryptography.fernet import Fernet as fer
import cryptography
import cryptography.fernet
import Connect


def ConsultKey():
    """
    consult the key to encrypt/decrypt messages\n
    @Return\n
        (binary): the masterkey 
    """
    conn = Connect.DB()
    cursor = conn.cursor()
    query = 'SELECT Key FROM KeyMaster'
    cursor.execute(query)
    key = cursor.fetchall()
    cursor.close()
    conn.close()
    return key[0][0]

def CreateInsertKeyMaster():
    """
    create the key master to encryot/decrypt \n
    all the data who needs to be encrypted, and keep it save
    """
    key = fer.generate_key()
    objfer = fer(key)
    conn = Connect.DB()
    cursor = conn.cursor()
    query = 'INSERT INTO KeyMaster (key) VALUES (?)'
    cursor.execute(query, (key,))
    conn.commit()
    cursor.close()
    conn.close()

def encryptMessage(message):
    """
    encrypt the string receved\n
    @Param\n
    message: string to encrypt
    """
    key = ConsultKey()
    e = message.encode()
    key = fer(key)
    i = key.encrypt(e)
    return i

def decrypt(message):
    """
    decrypt the message\n
    @Param\n
        message (byte): the message needs to be encrypted\n
    @Return\n
        (string):the message decrypted
    """
    key = ConsultKey()
    key = fer(key)
    try:
        i = key.decrypt(message)
        return i.decode()
    except cryptography.fernet.InvalidToken as error:
        print('Token Error: Wrong key value')