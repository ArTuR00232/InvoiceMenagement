import Connect
from flask import jsonify
import Encryption

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


