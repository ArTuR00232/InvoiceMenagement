import Connect
from flask import jsonify
import Encryption
import Code as restCode

def consults(Username='', Pass=''):
    """_summary_

    Args:
        Username (str): _description_. Defaults to ''.
        Pass (str): _description_. Defaults to ''.

    Returns:
        _type_: json Object
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

def delete(id):
    """
    this modeule is for delete an User.\n
    id 
    Args:
        id (int): is the idUser.
    Returns:
        _type_: string
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
