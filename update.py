from models import conexao
import pymongo
from getpass import getpass
from bson.objectid import ObjectId
from datetime import datetime


conexao = conexao()
client = conexao.get_client()
db = client["seginfo"]
terms = db['terms']
aceite = db['acceptance']

try:
    name= input("Enter username:")
    passw= getpass(prompt="Enter password:")
    user_collection = db["user"]
    user = user_collection.find_one({"username": name, "userpassword": passw})
    idsession = user["_id"]

    termos = db.terms.find_one({},sort=[( '_id', pymongo.DESCENDING )])
    conteudotermo=str(termos['conditions'])
    versiontermo=str(termos['version'])
    print(versiontermo)
    idtermo=str(termos['_id'])

    if idsession != None:
        validation = "ok"
        print("login concluido")
    else:
        validation = None
        print("acesso negado")
except Exception as e:
    validation = None
    print(f"Erro ao logar o usuário: {e}")

if(validation=="ok"):
    user_collection = db["user"]
    consentlist=[]

    checkmail=input("Deseja receber emails?")
    if checkmail == "sim":
        acceptemail=True
        consentlist.append("Envio de Emails")
        print("Envio de Emails ON")
    else:
        acceptemail=False
        print("Envio de Emails OFF")

    checksensible=input("Deseja user dados sensiveis?")
    if checksensible == "sim":
        acceptsensible=True
        consentlist.append("Uso de dados sensíveis")
        print("Uso de dados sensíveis ON")
    else:
        acceptsensible=False
        print("Uso de dados sensíveis OFF")

    checkads=input("Deseja customizar anuncios?")
    if checkads == "sim":
        acceptads=True
        consentlist.append("Personalização de anúncios")
        print("Personalização de anúncios ON")
    else:
        acceptads=False
        print("Personalização de anúncios OFF")

    consent= input("By typing OK button, you are creating an account, and agree to Terms of Service and Privacy Policy:")
    accept = {'userid': idsession, 'termid' : idtermo, 'user': name, 'version': versiontermo, 'date': datetime.now(),'acceptarray':consentlist}
    result = aceite.insert_one(accept)
    #user_collection.update_one({"_id": idsession}, {"$set": {"username": name, "usermail": mail}})
    print("Update concluido")
