from flask import Flask, jsonify
import User, Code as restCode
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
    print(result)
    return jsonify(result)

#Methods to insert
@app.route('/API/User/post/<string:username>+<string:passW>', methods = ['POST'])
def setUser(username, passW):
    result = User.singup(username, passW)
    return jsonify(result)

#Methods to update
@app.route('/API/User/update/<string:Iduser>+<string:pw>+<string:code>', methods = ['POST'])
def updatePass(Iduser, pw, code):
    result = User.update(pw, Iduser, code)
    return(result)


#Methods to Delete
@app.route('/API/User/delete/<string:idUser>', methods = ['DELETE'])
def delUser(idUser):
    print(idUser)
    User.delete(idUser)
    return(['TRUE'])


if __name__ == '__main__':
    app.run(debug=True)