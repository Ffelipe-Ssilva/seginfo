import getpass,pymongo
from models import conexao
from datetime import datetime
from flask import make_response
from bson import json_util, ObjectId
import json

conexao = conexao()
client = conexao.get_client()
db = client["seginfo"]

colecao = db['user']
terms = db['terms']
aceite = db['acceptance']

termos = db.terms.find_one({},sort=[( '_id', pymongo.DESCENDING )])
conteudotermo=str(termos['conditions'])
versiontermo=str(termos['version'])

idtermo=str(termos['_id'])


def createUser(request):
    consentlist = []
    if request.get('sensible') != "True" and ('eth' in request or 'gen' in request or 'age' in request):
        return make_response("Cannot save sensible values without user permission", 422)
    if request.get('sensible'):
        consentlist.append("Uso de dados sensíveis")
    if request.get('ads'):
        consentlist.append("Personalização de anúncios")
    if request.get('checkmail'):
        consentlist.append("Envio de Emails")
    if request.get('customAds'):
        consentlist.append("Personalização de anúncios")

    if request.get('sensible') != "True":
        data = {'username': request.get('name'), 'usermail' : request.get('mail'), 'userpassword': request.get('passw'), 'userrole': 'user','usergender': request.get('gen'), 'userethnicity': request.get('eth'), 'userage': request.get('age'), 'useradds': request.get('userads'), 'userpref': ''}
        createdUserId = colecao.insert_one(data).inserted_id
    else:
        data = {'username': request.get('name'), 'usermail' : request.get('mail'), 'userpassword': request.get('passw'), 'userrole': 'user', 'useradds': request.get('userads'), 'userpref': ''}
        createdUserId = colecao.insert_one(data).inserted_id

    createdUser = colecao.find_one({"_id": ObjectId(createdUserId)})

    acceptanceData = {'userid': createdUserId, 'termid' : idtermo, 'user': request.get('name'), 'version': versiontermo, 'date': datetime.now(),'acceptarray':consentlist}
    createdAcceptanceId = aceite.insert_one(acceptanceData).inserted_id
    createdAcceptance = aceite.find_one({"_id": ObjectId(createdAcceptanceId)})

    return {'user': json.loads(json_util.dumps(createdUser)), 'acceptance': json.loads(json_util.dumps(createdAcceptance))}