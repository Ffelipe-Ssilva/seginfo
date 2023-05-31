from models import conexao
import pymongo
from getpass import getpass
from bson.objectid import ObjectId
import pymongo
from pymongo import MongoClient
from datetime import datetime
import jwt

conexao = conexao()
client = conexao.get_client()
db = client["seginfo"]
colecao = db['sell']
acceptance= db['acceptance']

def checkLatestTerm(token):
    try:
        decodedToken = jwt.decode(token, 'secret', algorithms=["HS256"])
    except:
        return 'Unauthorized'
    print(decodedToken['_id']['$oid'])
    acceptquery = db.acceptance.find_one({'userid': ObjectId(decodedToken['_id']['$oid'])}, sort=[("_id", pymongo.DESCENDING)])
    latestaccept = int(acceptquery['version'])
    termos = db.terms.find_one({}, sort=[('_id', pymongo.DESCENDING)])
    versiontermo = int(termos['version'])

    if versiontermo>latestaccept:
        return {'userHasTerm': True}
    return {'userHasTerm': False}