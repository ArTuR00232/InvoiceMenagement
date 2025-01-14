import Connect
from flask import jsonify
import Encryption
import Code as restCode

def consults(Username='', Pass=''):
    """
    Args:\n
        Username (str): _description_. Defaults to ''.\n
        Pass (str): _description_. Defaults to ''.\n

    Returns:\n
        _type_: json Object\n
    """
    conn = Connect.DB()
    cursor = conn.cursor()

    query = 'SELECT * FROM Users WHERE username = ? '
    cursor.execute(query, (Username, ))
    df = cursor.fetchall()
    try:
        pw = Encryption.decrypt(df[0][2])
        if(pw != Pass):
            return[False]
        if(pw == Pass):
            list_user = [{
        'ID': row[0],
        'username': row[1],
        'Session': 'true',
         } for row in df]          
        cursor.close()
        conn.close()
        return jsonify(list_user)
    
    except:
        return[False]

def update(key, idUser, code):
    """
    this module is for update the data in table. \n
    key can be the pass or Username, depends the options.\n
    Args:\n
        key (string): password. \n
        idUser (int): idUser.\n
        code (string): Code for change pass.\n

    Returns:\n
        _type_: Json\n
    """
    key = Encryption.encryptMessage(key)
    conn = Connect.DB()
    cursor = conn.cursor()
    query = "UPDATE Users SET password = ? WHERE id\
            (SELECT Users.id FROM Users JOIN RestorePassCode\
            ON Users.id = RestorePassCode.iduser\
            WHERE Users.username = ? AND RestorePassCode.Code = ?)"
    cursor.execute(query,(key, username, code))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify([True])

def singup(username, Pass):
    """
    Made a singup an user in table.\n
    Args:
        username (string): User name  \n
        Pass (string): password\n
    """
    info = Encryption.encryptMessage(Pass)
    Pass = info
    conn = Connect.DB()
    cursor = conn.cursor()
    query = 'INSERT INTO Users (Username, password) VALUES (?,?)'
    cursor.execute(query, (username, Pass))
    conn.commit()
    cursor.close()
    conn.close()
    ids = userGetID(username)
    restCode.codeInsert(ids)


def delete(id):
    """
    This modeule is for delete an User.\n
    Args:\n
        id (int): is the idUser.\n
    Returns:\n
        _type_: string\n
    """
    conn = Connect.DB()
    cursor = conn.cursor()
    query = 'SELECT (username) FROM Users WHERE id = ?'
    cursor.execute(query, (id,))
    name = cursor.fetchall()
    query = 'DELETE FROM Users WHERE id = ?'
    cursor.execute(query,(id,))
    conn.commit()
    conn.close()
    restCode.codeDelete(id)
    return(name[0][0])

def userGetID(username):
    """
        consult an specific user and return the ID\n
    Args:\n
        username (string): user name\n

    Returns:\n
        _type_: int\n
    """
    conn = Connect.DB()
    cursor = conn.cursor()
    query = 'SELECT ID FORM Users WHERE username == ?'
    cursor.execute(query, (username,))
    conn.commit()
    df = cursor.fetchall()
    listUser = [{
        'ID':row[0],
    } for row in df]
    cursor.close()
    conn.close()
    id = df[0][0]
    return id
