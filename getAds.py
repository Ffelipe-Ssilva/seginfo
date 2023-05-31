from models import conexao
import pymongo
from getpass import getpass
from bson.objectid import ObjectId
import pymongo
from pymongo import MongoClient
from datetime import datetime
import jwt
import random

conexao = conexao()
client = conexao.get_client()
db = client["seginfo"]
colecao = db['sell']
acceptance= db['acceptance']

def getAds(token):
    try:
        decodedToken = jwt.decode(token, 'secret', algorithms=["HS256"])
    except:
        return 'Unauthorized'

    private = decodedToken['useradds']
    adslist=[]
    randomAds=[]

    randomAds.append("Celular - R$1000,00")
    randomAds.append("Notebook - R$3000,00")
    randomAds.append("Tablet - R$1500,00")
    randomAds.append("Smartwatch - R$800,00")
    randomAds.append("Televisão - R$4000,00")
    randomAds.append("Fones de ouvido - R$100,00")
    randomAds.append("Caixa de som - R$200,00")
    randomAds.append("Computador - R$5000,00")
    randomAds.append("Impressora - R$700,00")
    randomAds.append("Mouse - R$50,00")

    user = db.user.find_one({'_id': ObjectId(decodedToken['_id']['$oid'])})

    if private and decodedToken['userpref']:
        adslist.append("anuncio: ESPECÍFICO!!!")
        adslist.append(f"oferta de [" + user['userpref'] + "]")
        return adslist
    else:
        return random.choice(randomAds)