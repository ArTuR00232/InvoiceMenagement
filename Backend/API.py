from flask import Flask, jsonify
import User, Code as restCode, Money, Months, Marker
from flask_cors import CORS

app = Flask(__name__, template_folder = '../front/app/src',static_url_path=('/'))
CORS(app)

#methods to consult
@app.route('/Api/User/<string:Username>+<string:Pass>', methods =['GET'])
def getUser(Username, Pass):
    result = User.consults(Username,Pass)
    return(result)

@app.route('/API/code/<string:Code>+<string:IdUser>', methods = ['Get'])
def getVerificationCode(Code='', IdUser=''):
    result = restCode.codeConsult(Code, IdUser)
    return(result)

@app.route('/API/code/<string:id>', methods = ['GET'])
def getCode(id=''):
    result = restCode.consults(id)
    return jsonify(result[0])

@app.route('/API/Money/<string:IdUser>', methods = ['GET'])
def getMoney(IdUser):
    print(IdUser)

    result = Money.consults(IdUser)
    return (result)

@app.route('/API/Months/<string:Iduser>', methods = ['GET'])
def getMonths(Iduser = ''):
    result = Months.consults(Iduser)
    return(result)

@app.route('/API/Marker/<string:idUser>', methods = ['GET'])
def getMarker(idUser):
    result = Marker.consults(idUser)
    return jsonify(result)

#Methods to insert
@app.route('/API/User/post/<string:username>+<string:passW>', methods = ['POST'])
def setUser(username, passW):
    result = User.singup(username, passW)
    return jsonify(result)

@app.route('/API/Money/post/<string:Iduser>+<string:spend>+<string:date>+<string:description>', methods = ['POST'])
def setMoney(Iduser, spend, date, description):
    Money.insert(Iduser, spend, date, description)
    result = Money.consults(Iduser)
    return(result)

@app.route('/API/Marker/post/<string:idUser>+<string:name>+<string:color>', methods = ['POST'])
def setMarker(idUser, name, color):
    result = Marker.insert(idUser, name, color)
    return (result)


#Methods to update
@app.route('/API/User/update/<string:Iduser>+<string:pw>+<string:code>', methods = ['POST'])
def updatePass(Iduser, pw, code):
    result = User.update(pw, Iduser, code)
    return(result)

@app.route('/API/Money/update/<string:Iduser>+<string:Id>+<string:spend>+<string:date>+<string:marker>+<string:description>+<string:SpendOld>+<string:DateOld>', methods = ['POST'])
def updateMoney(Iduser, Id, spend, date, marker, description, SpendOld, DateOld):
    Money.update(Iduser, Id, spend, date, SpendOld, DateOld, marker,description)
    result = Money.consults(Iduser)
    return(result)

@app.route('/API/Marker/update/<string:id>+<string:name>+<string:color>', methods = ['POST'])
def updateMarker(id, name, color):
    result = Marker.update(name, color, id)
    return (result)


#Methods to Delete
@app.route('/API/User/delete/<string:idUser>', methods = ['DELETE'])
def delUser(idUser):
    print(idUser)
    User.delete(idUser)
    return(['TRUE'])

@app.route('/API/Money/delete/<int:id>', methods = ['DELETE','OPTIONS'])
def delMoney(id):
    Money.delete(id)
    return(['TRUE'])

@app.route('/API/Marker/delete/<int:id>', methods = ['DELETE','OPTIONS'])
def delMarker(id):
    Marker.delete(id)
    return(['TRUE'])



if __name__ == '__main__':
    app.run(debug=True)