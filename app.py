from flask import Flask, render_template, request
from waitress import serve
import re

from create import createUser
from login import loginUser
from delete import deleteUser
from readmydata import findUser, importUser
from update import updateUser
from readcobranca import mailing
from checkLatestTerm import checkLatestTerm
from signTerm import signTerm
from getAds import getAds
from buyProduct import buyProduct

app = Flask(__name__)
app.secret_key = 'app_secret'

@app.route('/user', methods=['POST'])
def userCreate():
    return createUser(request.json)

@app.route('/user', methods=['PATCH'])
def updateCreate():
    return updateUser(request.json, request.headers.get('Authorization'))

@app.route('/user', methods=['GET'])
def find():
    return findUser(request.headers.get('Authorization'))

@app.route('/checkTerm', methods=['GET'])
def checkTerm():
    return checkLatestTerm(request.headers.get('Authorization'))

@app.route('/signTerm', methods=['POST'])
def signLatestTerm():
    return signTerm(request.json, request.headers.get('Authorization'))

@app.route('/buyProduct', methods=['POST'])
def sellProduct():
    return buyProduct(request.json, request.headers.get('Authorization'))

@app.route('/ads', methods=['GET'])
def findAds():
    return getAds(request.headers.get('Authorization'))

@app.route('/mail', methods=['GET'])
def mail():
    return mailing(request.headers.get('Authorization'))

@app.route('/user/login', methods=['POST'])
def userLogin():
    return loginUser(request.json)

@app.route('/importuser', methods=['POST'])
def userImport():
    return importUser(request.json)

@app.route('/user/<userId>', methods=['DELETE'])
def delete(userId=None):
    response = deleteUser(userId, request.headers.get('Authorization'))
    if(response == 'Unauthorized'):
        return app.response_class(
            response= 'Unauthorized',
            status=401
        )
    if(response == 'Not_Found'):
        return app.response_class(
            response= 'User not found',
            status=404
        )
    if(response == 'Deleted'):
        return app.response_class(
            response= 'User has been deleted',
            status=200
        )

if __name__ == '__main__':
    serve(app, host='127.0.0.1',port=5000)