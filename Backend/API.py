from flask import Flask, jsonify
import User
from flask_cors import CORS

app = Flask(__name__, template_folder = '../front/app/src',static_url_path=('/'))
CORS(app)

#methods to consult
@app.route('Api/User/<string:Username>+<string:Pass>', methods =['GET'])
def getuser(Username, Pass):
    result = User.consults(Username,Pass)
    return(result)

if __name__ == '__main__':
    app.run(debug=True)