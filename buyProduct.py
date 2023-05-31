from models import conexao
import pymongo
from getpass import getpass
from bson.objectid import ObjectId
import pymongo
from pymongo import MongoClient
from datetime import datetime
from bson import json_util, ObjectId
import json
import jwt
import random

conexao = conexao()
client = conexao.get_client()
db = client["seginfo"]
colecao = db['sell']
acceptance= db['acceptance']

def buyProduct(request, token):
    try:
        decodedToken = jwt.decode(token, 'secret', algorithms=["HS256"])
    except:
        return 'Unauthorized'

    user = db.user.find_one({'_id': ObjectId(decodedToken['_id']['$oid'])})
    private = user['useradds']

    dados = {'sellprod': request.get('prodDesc'), 'sellprice' : request.get('price'), 'userpassword': decodedToken['_id']['$oid']}
    result = colecao.insert_one(dados).inserted_id
    createdSell = colecao.find_one({"_id": ObjectId(result)})

    if private:
        personalizar = db['user']
        myquery = {"_id": ObjectId(decodedToken['_id']['$oid'])}
        newvalues = {"$set": {"userpref": str(request.get('prodDesc'))}}
        personalizar.find_one_and_update(myquery, newvalues)

    return json.loads(json_util.dumps(createdSell))