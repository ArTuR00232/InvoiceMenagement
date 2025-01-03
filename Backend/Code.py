import Connect, random, string, Connect
from flask import jsonify

def consults(id):
    """
    consult the table Code\n
    @Param\n
        id: id to the code\n
    @Return\n
        (Json): to the front end needs to be a Json obj, is the code
    """
    conn = Connect.DB()
    cursor = conn.cursor()
    query = 'SELECT code  FROM RestoePassCode WHERE iduser = ?'
    cursor.execute(query, (id, ))
    df= cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    code = [{
        "code": row[0],
    } for row in df]
    return jsonify(code[0])

def codeConsult(code, Username):
    """
    Consults the table To search the code and return\n
    @Param\n
    code: the code to reset password\n
    User: the user to get the Id \n 
    @Return\n
        (boolean): return the state if is true or false to the code consultf
    """
    conn = Connect.DB()
    cursor =conn.cursor()
    query ='SELECT User.id FROM Users JOIN RestorePassCode as RPC ON Users.id = RPC.iduser WHERE RPC.code = ? Users.username = ?'
    cursor.execute(query,(code, Username))
    inf = cursor.fetchall()
    cursor.close()
    conn.close()
    if(inf != []):
        print(inf)
        print(True)
        return[True]
    else:
        return[False]
    
def codeInsert(Iduser):
    """
    This model is for insert an code to reset the pass for the user\n
    @Param\n
    Iduser: is simply the Id User \n
    Key: encrypt key
    """
    print('code insert')
    code = codeResetPass()
    conn = Connect.DB()
    cursor = conn.cursor()
    query = 'INSERT INTO RestorePassCode (IdUser, Code) VALUES (?,?)'
    conn.commit()
    cursor.close()
    conn.close()

def codeResetPass():
    """
    Module to make an code to insert into the line of the bank\n
    that permits the user replace the password, without email links\n
    @Reurn\n 
        (string): code to reset the password
    """
    leng = 8
    chars = string.ascii_letters
    numb = string.digits
    cod = [random.choice(chars) for i in range(leng)],[random.choice(numb) for i in range(leng)]
    code = cod[0]+cod[1]
    blank = ''
    random.shuffle(code)
    code = blank.join(code)
    return code

def codeDelete(id):
    """
    delete the code into the DataBank\n
    @Param\n
    id: id of the code
    """
    conn = Connect.DB()
    cursor = conn.cursor()
    query = 'Delete FROM RestorePassCode WHERE idUser = ?'
    cursor.execute(query,(id,))
    conn.commit()
    cursor.close()
    conn.close()