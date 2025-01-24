import Connect
from flask import jsonify

def consults(idUser):
    """
    Consult the table.\n
    opt id the iduser, but is optional\n
    Args:\n
        idUser (int): user ID\n
    Returns:\n
        Json list: infos about spend of the user
    """
    conn = Connect.DB()
    cursor = conn.cursor()
    query = 'SELECT * FROM Bank WHERE iduser = ?'
    cursor.execute(query,(idUser,))
    df = cursor.fetchall()
    list_df = [{
        'Id': row[3],
        'Iduser': row[0],
        'TotalSpend': row[2],
        'Data': row[1],
    } for row in df]
    conn.close()
    return jsonify(list_df)
def update(iduser, date, spendOld='', dateOld=''):
    """
    This module is for update the total spend of the table.\n
    iduser, is the id of the user.\n
    date is the exatly month that will be updated.\n
    Args:\n
        iduser (int): id User.\n
        date (string): date of the spend.\n
        spendOld (str, optional): old spend of the row. Defaults to\n ''.
        dateOld (str, optional): old date of the row. Defaults to\n ''.
    """
    Date = date[:-3]
    conn = Connect.DB()
    cursor = conn.cursor()
    reg_info_del = sum(iduser,date[:-3])
    if(dateOld == ''):
        if(reg_info_del == 0):
            delete(iduser,date)
        else:
            query = 'SELECT id FROM Bank WHERE DateM = ?'
            cursor.execute(query,(Date,))
            ids = cursor.fetchall()
            #get the calue spend in the new date
            total = sum(iduser, Date)
            query = 'UPDATE Bank SET SpendM = ?, DateM = ? WHERE id = ?'
            cursor.execute(query, (total,Date, ids[0][0]))
            conn.commit()
    else:
        DateOld = dateOld[:-3]
        query = 'SELECT id FROM Bank WHERE DateM = ?'
        cursor.execute(query,(DateOld,))
        ids = cursor.fetchall()
        #get the value spend in the new date
        total = sum(iduser, Date)
        query = 'UPDATE Bank SET SpendM = ?, DateM = ? WHERE id = ?'
        cursor.execute(query,(total, Date, ids[0][0]))
        conn.commit()
    cursor.close()
    conn.close()

def insert(IdUser, Month):
    """
    Insert data in the table.\n
    Args:\n
        IdUser (int): user id.\n
        Month (string): year-Month.\n
    """
    conn = Connect.DB()
    cursor = conn.cursor()
    total = sum(IdUser, Month)
    query = 'INSERT INTO Bank (iduser, SpendM, DateM) VALUES(?,?,?)'
    cursor.execute(query,(IdUser, total, Month))
    conn.commit()
    conn.close()

def insertOrUpdate(idUser ='', date='', spendOld='',dateOld='',id = ''):
    """
    Defines if its will be an insert or an update of the bank(total spend in a month).\n
    id is id of the month, if don't have it will be create.\n
    Args:\n
        idUser (str, optional): user id . Defaults to ''.\n
        date (str, optional): the new date of the Item. Defaults to ''.\n
        spendOld (str, optional): old spend of the Item. Defaults to ''.\n
        dateOld (str, optional): old date of the Item. Defaults to ''.\n
        id (int): is the id of the row.\n
    """
    conn = Connect.DB()
    cursor = conn.cursor()
    reg = sum(idUser, dateOld)
    query = 'SELECT ID FROM Bank WHERE  DateM = ? AND  iduser = ?'
    cursor.execute(query,(date[:-3], idUser))
    ids = cursor.fetchall()
    if(dateOld == ''):
        if(ids == []):
            insert(idUser, date[:-3])
        else:
            reg_Money = sum(idUser, date[:-3])
            if(reg_Money == 0):
                delete(idUser, date)
            else:
                update(idUser, date)
    else:
        if(ids != []):
            update(idUser, date)
            if(reg == 0):
                delete(idUser,dateOld)
            else:
                update(idUser, date = dateOld, spendOld = spendOld)
        else:
            regOld = sum(idUser, dateOld[:-3])
            if(regOld == 0):
                update(idUser, date, spendOld, dateOld)
            else:
                update(idUser, date = dateOld, spendOld = spendOld)
                insert(idUser, date[:-3])
    cursor.close()
    conn.close()

def sum(idUser, date):
    """
    Delete an data from the table according to user id and date.\n
    Args:\n
        idUser (int): user id.\n
        date (string): exatly month to delete "year-moth".\n
    Returns:\n
        int: sum of amounts spend of the month.\n
    """
    dat = '%'+date+'%'
    conn = Connect.DB()
    cursor = conn.cursor()
    query = 'SELECT SUM(Spend) FROM Money WHERE Date LIKE ? AND iduser = ?'
    cursor.execute(query,(dat, idUser,))
    result = cursor.fetchall()
    result = result[0][0]
    if(result == None):
        result = 0
    return round(result,2)

def delete(idUser, date = ''):
    """
    Delete an data from the table according to user id and date.\n
    Args:\n
        idUser (int): user Id\n
        date (str, optional): the exatly motnh to delete "year-month". Defaults to ''.\n
    """
    conn = Connect.DB()
    cursor = conn.cursor()
    if(len(date)>7):
        date = date[:-3]
    if(date != ' '):
        query = 'DELETE FROM Bank WHERE iduser = ? AND DateM = ?'
        cursor.execute(query, (idUser, date))
    else:
        query = 'DELETE FROM Bank WHERE iduse = ?'
        cursor.execute(query,(idUser,))
    conn.commit()
    cursor.close()
    conn.close()
