import Connect
from flask import jsonify, request
import Marker, Months

def consults(idUser):
    """
        Consult the table.\n
    Args:\n
        idUser (int):\n 

    Returns:\n
        (Json): json with all the informations that the front end need.
    """
    conn = Connect.DB()
    cursor = conn.cursor()
    query = 'SELECT Money.id, Date, Spend, Description, name, color from Money JOIN marker on Money.marker_id = marker.id WHERE Money.iduser = ?'
    cursor.execute(query, (idUser,))
    df = cursor.fetchall()

    list_df=[{
        'Id': row[0],
        'Spended': row[2],
        'Date': row[1],
        'Description': row[3],
        'Marker':row[4],
        'Color':row[5]
    } for row in df]
    conn.close()
    return jsonify(list_df)

def update(IdUser, id, spend, date, spendOld, dateOld, marker, description =''):
    """
    This module is for update the data of the table.\n
    Args:\n
        IdUser (int): id of the user \n
        id (int): is the id of the data\n
        spend (str): money spended updated\n
        date (str): date when spended the money\n
        spendOld (str): the wrong date (was modified by user)\n
        dateOld (str): the wrong date (was modified by user)\n
        marker (str):nameof the marker.\n
        description (str, optional): Description updated. Defaults to ''.\n

    Returns:\n
        int: user id
    """
    print('update Money')
    conn = Connect.DB()
    if(description =='Null'):
        description = ''
    if(spend == '0'):
        delete(id)
    if(description != 'Null'):
        marker_data = Marker.consults(IdUser, marker)
        if(marker_data == False):
            query = ('UPDATE Money SET Date = ?, Spend = ?, Description = ? WHERE id = ?')
            cursor = conn.cursor()
            cursor.execute(query,(date, spend, description, id))

        if(marker_data != False):
            marker_data = marker_data[0].values()
            idMarker = marker_data.mapping.get('id')
            query = ('UPDATE Money SET Date = ?, Spend = ?, Description = ?, marker_id = ? WHERE id = ?')
            cursor = conn.cursor()
            cursor.execute(query, (date,spend, description, idMarker, id))
        
    
    conn.commit()
    conn.close()
    Months.insertOrUpdate(IdUser, date, spendOld, dateOld, id)

def insert(IdUser, spend, date, description=''):
    """_summary_
    insert data in the table Money.\n

    Args:\n
        IdUser (int): user id \n
        spend (float): the money spent.\n
        date (str): date that the user spend money\n
        description (str, optional): Defaults to ''.\n

    Returns:\n
        int: id User
    """
    
    if(description ==' Null'):
        description =''
    print('insert money')
    conn =  Connect.DB()
    cursor = conn.cursor()
    marker = Marker.consults(IdUser,'general')
    marker_id = marker[0].get('id')
    query = 'INSERT INTO Money (iduser, Spend, Date, Description, marker_id) Values (?,?,?,?,?)'
    cursor.execute(query,(IdUser, spend, date, description, marker_id))
    conn.commit()
    cursor.close()
    conn.close()
    Months.insertOrUpdate(IdUser, date)
    result = consults(IdUser)
    return result
    
def delete(id = '', idUser =''):
    """
    delete data in the table Money.\n
    Args:\n
        id (str, optional): spend id. Defaults to ''.\n
        idUser (str, optional): is of the user. Defaults to ''.\n
    """
    conn = Connect.DB()
    cursor = conn.cursor()
    if(id != ' '):
        query = 'SELECT iduser, Date FROM Money WHERE id = ?'
        cursor.execute(query,(id,))
        data = cursor.fetchall()
        query = 'DELETE FROM Money WHERE id = ?'
        cursor.execute(query,(id,))
        conn.commit()
        iduser = data[0][0]
        date = data[0][1]
        Months.insertOrUpdate(iduser, date, id=id)

    if(idUser !=' '):
        query ='DELETE FROM Money WHERE iduser = ?'
        cursor.execute(query,(idUser,))
        conn.commit()
        Months.delete(idUser)
    cursor.close()
    conn.close()