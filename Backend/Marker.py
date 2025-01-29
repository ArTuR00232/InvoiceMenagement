import Connect
from flask import jsonify
import Money

def consults(iduser, name = ''):
    """
    consult the marker table \n
    Args\n:
        iduser (int): user ID\n
        name (str, optional): marker name. Defaults to ''.\n
    Returns:\n
        list: list with the info about the markers.
    """
    conn = Connect.DB()
    cursor = conn.cursor()
    if(name == ''):
        query = ('SELECT id, name, color FROM marker WHERE idUser =?')
        cursor.execute(query, (iduser,))
        df = cursor.fetchall()
        list_marker = [{
            'id': row[0],
            'name':row[1],
            'color':row[2]
        } for row in df]
        return list_marker
    if(name != ''):
        query = ('SELECT id, name, color FROM marker WHERE  idUser = ? AND name = ?')
        cursor.execute(query,(iduser, name))
        df = cursor.fetchall()
        list_marker = [{
            'id':row[0],
            'name':row[1],
            'color':row[2]
        }for row in df]
        if(df == []):
            return False
        else:
            return (list_marker)
        
def insert(id, name, color):
    """
    Insert into the table marker \n
    Args:\n
        id (int): id user\n
        name (str): name of the marker\n
        color (str): hash of the color\n
    """
    conn = Connect.DB()
    cursor = conn.cursor()
    color = '#' + color
    query = ('INSERT INTO marker (name, color, idUser) VALUES(?,?,?)')
    cursor.execute(query,(name, color, id))
    conn.commit()
    conn.close()
    cursor.close()
    return(True)

def update(name, color = '', id = ''):
    """
    Update the table marker\n
    Args:\n
        name (str): name of the marker.\n
        color (str, optional): hash of the selected color. Defaults to ''.\n
        id (int):  id od hte marker.

    """
    conn = Connect.DB()
    cursor = conn.cursor()
    query = 'UPDATE marker SET name = ?, color = ? WHERE id = ?'
    cursor.execute(query,(name, color, id))
    print('update')
    conn.commit()
    cursor.close()
    conn.close()

def delete(id, iduser):
    """
    module to delete from table marker\n
    Args:\n
        id (int): id of the marker.\n
    Returns:\n
        str: returs true when the marker is deleted
    """
    conn = Connect.DB()
    cursor = conn.cursor()
    query = 'SELECT id FROM marker WHERE idUser = ? AND name = "general"'
    cursor.execute(query,(iduser,))
    df = cursor.fetchall()
    if(df != []):
        query = 'UPDATE Money SET marker_id = ? WHERE marker_id = ?'
        cursor.execute(query,(df[0][0], id))
        conn.commit()
    query = 'DELETE FROM marker WHERE id = ?'
    cursor.execute(query,(id,))
    conn.commit()
    cursor.close()
    conn.close()
    return ('True')

def deleteAll(idUser):
    """
    Delete all the markers related with the current user.\n
    Args:\n
        idUser (int): user Id\n
    """
    conn = Connect.DB()
    cursor = conn.cursor()
    query = ('DELETE FROM marker WHERE idUser = ?')
    cursor.execute(query,(idUser,))
    conn.commit()
    cursor.close()
    conn.close()

