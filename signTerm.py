from models import conexao
import pymongo
from getpass import getpass
from bson.objectid import ObjectId
import pymongo
from pymongo import MongoClient
from datetime import datetime
import jwt
from bson import json_util, ObjectId
import json

conexao = conexao()
client = conexao.get_client()
db = client["seginfo"]
colecao = db['sell']
acceptance= db['acceptance']

def signTerm(request, token):
    try:
        decodedToken = jwt.decode(token, 'secret', algorithms=["HS256"])
        print(decodedToken)
    except:
        return 'Unauthorized'

    termos = db.terms.find_one({}, sort=[('_id', pymongo.DESCENDING)])

    consentlist= []
    if request.get('sensible'):
        consentlist.append("Uso de dados sensíveis")
    if request.get('checkmail'):
        consentlist.append("Envio de Emails")
    if request.get('customAds'):
        consentlist.append("Personalização de anúncios")

    accept = {'userid': decodedToken['_id']['$oid'], 'termid': termos['_id'], 'user': decodedToken['username'], 'version': termos['version'], 'date': datetime.now(),
              'acceptarray': consentlist}
    acceptId = acceptance.insert_one(accept).inserted_id
    createdAcceptance = acceptance.find_one({"_id": ObjectId(acceptId)})
    return json.loads(json_util.dumps(createdAcceptance))