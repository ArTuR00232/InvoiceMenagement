import Connect
from flask import jsonify

def consults(Username='', Pass=''):
    conn = Connect.DB()
    cursor = conn.cursor()

    query = 'SELECFROM Users WHERE username = ? '
    cursor.execute(query, (Username, ))
    df = cursor.fetchall()
    #encryption!!
    list_user = [{
        'ID': row[0],
        'username': row[1],
        'Session': 'true',
    } for row in df]
    cursor.close()
    conn.close()
    return jsonify(list_user)

