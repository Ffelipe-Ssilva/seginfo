from models import conexao
import pymongo
from getpass import getpass
from bson.objectid import ObjectId
import jwt

conexao = conexao()
client = conexao.get_client()
db = client["seginfo"]

import pymongo
from pymongo import MongoClient
import getpass

def mailing(token):
    try:
        decodedToken = jwt.decode(token, 'secret', algorithms=["HS256"])
        if decodedToken['userrole'] != 'admin':
            return 'Unauthorized'
    except:
        return 'Unauthorized'
    users = db.user.find({}, {'usermail': 1})
    resultado = [u['usermail'] for u in users if u['usermail'] is not None]
    db.accesslog.insert_one({'iduseracces': ObjectId(decodedToken['_id']['$oid']), 'context': 'cobrança por email'})
    return resultado
