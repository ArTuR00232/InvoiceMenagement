import Connect
from flask import jsonify, request

def consults(idUser):
    """
        Consult the table.\n
    Args:\n
        idUser (int):\n 

    Returns:\n
        (Json): json with all the informations that the front end need

    """
    conn = Connect.DB()
    iduser = request.args.get('idUser', idUser )
    cursor = conn.cursor()
    query = 'SELECT Money.id, Date, Spend, Description, name, color from Money WHERE Money.iduser = ?'
    cursor.execute(query, (f'{idUser}'))
    df = cursor.fetchall()

    list_df=[{
        'Id': row[0],
        'Spended': row[2],
        'Date': row[1],
        'Description': row[3],
    } for row in df]
    conn.close()
    return jsonify(list_df)

def update(IdUser, id, spend, date, spendOld, description =''):
    """
    This module is for update the data of the table.\n
    Args:\n
        IdUser (int): id of the user \n
        id (int): is the id of the data\n
        spend (str): money spended updated\n
        date (str): date when spended the money\n
        spendOld (str): the wrong date (was modified by user)\n
        description (str, optional): Description updated. Defaults to ''.\n

    Returns:\n
        int: user id
    """
    
    conn = Connect.DB()
    if(description =='Null'):
        description = ''
    if(spend == '0'):
        delete(id)
    else:
        cursor = conn.cursor()
        query = 'UPDATE Money SET Date = ?, Spend = ?, Description = ? WHERE id = ?'
        cursor.execute(query, (date, spend, description, id))
    
    conn.commit()
    conn.close()

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
        print('insert')
        conn =  Connect.DB()
        cursor = conn.cursor()
        query = 'INSET INTO Money (iduser, Spend, Date, Description), Values (?,?,?,?)'
        cursor.execute(query,(IdUser, spend, date, description))
        conn.commit()
        cursor.close()
        conn.close()

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
            query = 'DELETE DROM Money WHERE id = ?'
            cursor.execute(query,(id,))
            conn.commit()
            print('delete')

        if(idUser !=' '):
            query ='DELETE FROM Money WHERE iduser = ?'
            cursor.execute(query,(idUser,))
            conn.commit()
        cursor.close()
        conn.close()
