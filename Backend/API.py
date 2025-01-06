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
    return(result)


if __name__ == '__main__':
    app.run(debug=True)