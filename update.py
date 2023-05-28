from models import conexao
import pymongo
from getpass import getpass
from bson.objectid import ObjectId
from datetime import datetime
import jwt
from bson import json_util, ObjectId
import json

conexao = conexao()
client = conexao.get_client()
db = client["seginfo"]
terms = db['terms']
aceite = db['acceptance']
user_collection = db["user"]

def updateUser(request,token):
    try:
        decodedToken = jwt.decode(token, 'secret', algorithms=["HS256"])
    except():
        return 'Unauthorized'
    termos = db.terms.find_one({}, sort=[('_id', pymongo.DESCENDING)])
    versiontermo = str(termos['version'])
    idtermo = str(termos['_id'])
    consentlist= []

    if request.get('sensible'):
        consentlist.append("Uso de dados sensíveis")
    if request.get('ads'):
        consentlist.append("Personalização de anúncios")
    if request.get('checkmail'):
        consentlist.append("Envio de Emails")
    if request.get('customAds'):
        consentlist.append("Personalização de anúncios")

    accept = {'userid': ObjectId(decodedToken['_id']['$oid']), 'termid': idtermo, 'user': request.get('name'), 'version': versiontermo, 'date': datetime.now(),'acceptarray': consentlist}

    result = aceite.insert_one(accept).inserted_id
    createdUser = aceite.find_one({"_id": ObjectId(result)})
    return json.loads(json_util.dumps(createdUser))
